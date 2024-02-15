import frappe

def get_menu_list():
	return []

@frappe.whitelist()
def get_menulist():
	domain = None
	try:
		domain = frappe.get_request_header('host')
	except Exception as e:
		pass
	user = frappe.session.user
	roles = frappe.get_roles(user)
	
	docs = []
	reports = []
	pages = []
	if roles:
		permitted_docs = ""
		for role in roles:
			# check for doctypes
			doc_perm = get_permitted_docs_for_role(role)
			docs += [x.parent for x in doc_perm]
			# check for report & page
			reports += get_permitted_pages_reports(role, 'Report')
			pages += get_permitted_pages_reports(role, 'Page')
	if docs:
		docs_list = list(set(docs))
		permitted_docs = ','.join(['"' + str(i) + '"' for i in docs_list])
	else:
		permitted_docs = '""'
	if reports:
		reports_list = list(set(reports))
		permitted_reports = ','.join(['"' + str(i) + '"' for i in reports_list])
	else:
		permitted_reports = '""'
	if pages:
		pages_list = list(set(pages))
		permitted_pages = ','.join(['"' + str(i) + '"' for i in pages_list])
	else:
		permitted_pages = '""'
	from frappe.core.doctype.domain_settings.domain_settings import get_active_domains
	domains_list = get_active_domains()
	if domains_list and len(domains_list) > 0:
		active_domain = ", ".join(['"' + i + '"' for i in domains_list if i])
	else:
		active_domain = '""'
	if not active_domain:
		active_domain = '""'
	query = """SELECT name, label as module_name, label, has_sub_menu, is_static_link, 
				static_link, menu_icon, menu_type, menu_doc, is_single_doc, menu_group,icon_image
				FROM `tabSide Menu` WHERE disable=0 
				order by sequence_number asc""".format(active_domain=active_domain,permitted_docs=permitted_docs)
	menu = frappe.db.sql(query, as_dict=1)
	menu_items_list = []
	
	if menu:
		for n in menu:
			n.has_sublist = 0
			if n.has_sub_menu:
				n.submenu = frappe.db.sql('''SELECT distinct sub_menu_title from `tabSub Menu` where parent=%s and disable=0 group by sub_menu_title order by idx asc''',n.name,as_dict=1)
				for k in n.submenu:
					subquery = '''SELECT s.sub_menu_type,s.sub_menu_doc,s.sub_menu_label,s.report_type,s.sub_menu_icon,s.is_single,s.is_static_link,s.static_link 
								FROM `tabSub Menu` s where s.parent=%s and s.disable=0 and s.sub_menu_title=%s 
								and (case when s.is_static_link=0 and s.sub_menu_type="DocType" then s.sub_menu_doc in ({permitted_docs}) else 1=1 end) 
								and (case when s.is_static_link=0 and s.sub_menu_type="Report" then s.sub_menu_doc in ({permitted_reports}) else 1=1 end) 
								and (case when s.is_static_link=0 and s.sub_menu_type="Page" then s.sub_menu_doc in ({permitted_pages}) else 1=1 end)
								and (case when s.is_static_link=1 and s.sub_menu_type="DocType" then s.sub_menu_doc in ({permitted_docs}) else 1=1 end) 
								and (case when s.is_static_link=1 and s.sub_menu_type="Report" then s.sub_menu_doc in ({permitted_reports}) else 1=1 end) 
								and (case when s.is_static_link=1 and s.sub_menu_type="Page" then s.sub_menu_doc in ({permitted_pages}) else 1=1 end)
								order by s.idx asc'''.format(active_domain=active_domain,permitted_docs=permitted_docs,permitted_reports=permitted_reports,permitted_pages=permitted_pages)
					k.sub_menu_list = frappe.db.sql(subquery, (n.name, k.sub_menu_title), as_dict=1)
					if len(k.sub_menu_list)>0:
						n.has_sublist=n.has_sublist+1
			else:
				if not n.is_static_link:
					if n.menu_type == 'DocType' and n.menu_doc not in permitted_docs:
						continue
					if n.menu_type == 'Report' and n.menu_doc not in permitted_reports:
						continue
					if n.menu_type == 'Page' and n.menu_doc not in permitted_pages:
						continue
				else:
					if n.menu_type == 'DocType' and n.menu_doc and n.menu_doc not in permitted_docs:
						continue
					if n.menu_type == 'Report' and n.menu_doc and n.menu_doc in permitted_reports:
						continue
					if n.menu_type == 'Page' and n.menu_doc and n.menu_doc in permitted_pages:
						continue
			menu_items_list.append(n)
	
	theme, enable_detail_left_menu, enable_list_left_menu = None, None, None
	for x in menu_items_list:
		if x.menu_type=="DocType":
			x.route = x.menu_doc.replace(" ", "-").lower()
		if x.menu_type=="Page":
			if x.is_static_link:
				x.route = x.menu_doc.replace(" ", "-").lower()
		if x.menu_type=="Report":
			x.route = "query-report/"+x.menu_doc
		if x.has_sub_menu:
			for mg in x.submenu:
				for m in mg.sub_menu_list:
					 if m.sub_menu_type=="DocType":
					 	m.route = m.sub_menu_doc.replace(" ", "-").lower()
					 if m.sub_menu_type=="Page":
					 	if m.is_static_link:
					 		m.route = m.sub_menu_doc.replace(" ", "-").lower()
					 if m.sub_menu_type=="Report":
					 	m.route = "query-report/"+m.sub_menu_doc
	side_menu_type = frappe.db.get_single_value("Side Menu Settings","select_side_menu_type")
	if side_menu_type == 'Side Menu':
		side_menu_settings = frappe.get_single('Side Menu Settings')
		side_menu_html = frappe.render_template("templates/side_menu1.html",{"menulist":menu_items_list,"user_info":frappe. get_user().doc,"side_menu_settings":side_menu_settings})
		return {"menu":menu_items_list,"enable_detail_left_menu":enable_detail_left_menu,"enable_list_left_menu":enable_list_left_menu,"template_html":side_menu_html,"side_menu_settings":side_menu_settings}
	elif side_menu_type == 'Drill Down Menu':
		side_menu_settings = frappe.get_single('Side Menu Settings')
		side_menu_html = frappe.render_template("templates/drill_down_menu.html",{"menulist":menu_items_list,"user_info":frappe. get_user().doc,"side_menu_settings":side_menu_settings})
		return {"menu":menu_items_list,"enable_detail_left_menu":enable_detail_left_menu,"enable_list_left_menu":enable_list_left_menu,"template_html":side_menu_html,"side_menu_settings":side_menu_settings}
	elif side_menu_type == 'Side Menu With Tab':
		side_menu_settings = frappe.get_single('Side Menu Settings')
		side_menu_html = frappe.render_template("templates/drill_down_tab.html",{"menulist":menu_items_list,"user_info":frappe. get_user().doc,"side_menu_settings":side_menu_settings})
		return {"menu":menu_items_list,"enable_detail_left_menu":enable_detail_left_menu,"enable_list_left_menu":enable_list_left_menu,"template_html":side_menu_html,"side_menu_settings":side_menu_settings}

def get_permitted_docs_for_role(role):
	perms = frappe.get_all('DocPerm', fields='parent', filters=dict(role=role))
	custom_perms = frappe.get_all('Custom DocPerm', fields='parent', filters=dict(role=role))
	doctypes_with_custom_perms = frappe.db.sql_list("""select distinct parent
		from `tabCustom DocPerm`""")

	for p in perms:
		if p.parent not in doctypes_with_custom_perms:
			custom_perms.append(p)
	return custom_perms

@frappe.whitelist()
def get_permitted_pages_reports(role, parenttype):
	'''
		To check report & page permission

		param: role: user role
		param: parenttype: Check whether report or page - Report, Page 
	'''
	perms = frappe.db.sql_list('''select parent from `tabHas Role` where parenttype = %(type)s and role = %(role)s''',{'type': parenttype, 'role': role})
	custom_perms = frappe.db.sql_list('''select c.report from `tabCustom Role` c inner join `tabHas Role` h on h.parent=c.name where h.role = %(role)s and c.{field} is not null'''.format(field = ('report' if parenttype == 'Report' else 'page')),{'role': role})
	if custom_perms:
		perms += custom_perms
	return perms


# Kishore
@frappe.whitelist(allow_guest=True)
def get_all_records(doctype, limit_start=0, limit_page_length=10):
    try:
        data = frappe.get_list(doctype, fields=["*"], start=limit_start, page_length=limit_page_length)
        return data
    except Exception as e:
        # frappe.log_error(f"Error in get_all_records for {doctype}", e)
        return []

@frappe.whitelist(allow_guest=True)
def get_list():
	data = frappe.get_list('Project', fields=["*"])
	for i in data:
		x = i.columns
		return x

@frappe.whitelist(allow_guest=True)
def get_doctype():
	side_menu_type = frappe.db.get_single_value("Side Menu Settings","select_side_menu_type")
	return side_menu_type


@frappe.whitelist(allow_guest=True)
def set_default_route():
	route = frappe.db.get_single_value("Side Menu Settings","route_logo")
	frappe.log_error("route", route)
	frappe.local.response['home_page'] ="/app/"+route

