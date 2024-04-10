import frappe ,requests, json
from frappe import _

def get_context():
	userId = frappe.form_dict.userId
	login_erp(userId)

@frappe.whitelist()
def login_erp(userId):
		import frappe.sessions
		from frappe.desk.notifications import clear_notifications
		from frappe.website.utils import clear_website_cache
		site = frappe.local.site
		if site:
			try:
				frappe.connect(site)
				frappe.clear_cache()
				# clear_notifications()
				# clear_website_cache()
			finally:
				frappe.destroy()
		try:
			data = {
				"userId": userId
			}
			userCred = requests.post(url="https://supplierapi.tasmace2euat.in:5008/api/WebUser/GetUser",json=data)
			frappe.log_error("Resp",userCred.json())
			userCredJSON = userCred.json()
			# json = {
			#     "usr":userCredJSON['data'][0].get('userName'),
			#     "pwd":userCredJSON['data'][0].get('password')
			# }
			# frappe.log_error("jsonnnn",json)
			if userCredJSON['data']:
				check_user = frappe.db.get_all("User",filters={"username":userCredJSON['data'][0].get('userName')})
				if check_user:
					from frappe.sessions import clear_sessions
					clear_sessions(user=check_user[0].name, keep_current=True, force=True)
					frappe.local.login_manager.user = check_user[0].name
					# frappe.local.login_manager.authenticate(userCredJSON['data'][0].get('userName'), userCredJSON['data'][0].get('password'))
					frappe.local.login_manager.post_login()

			# res = requests.post(url= frappe.utils.get_url() + "/api/method/login",json=json)
			# frappe.log_error("Res",res.status_code)
			# if res.status_code != 200:
			#     frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)
			# frappe.local.flags.redirect_location= "/app"
			# raise frappe.Redirect
			
			# sid = res.cookies.get("sid")
			# # frappe.log_error("get session id",res.cookies.get("sid"))
			# return sid
		except Exception:
			frappe.log_error("erplogin",frappe.get_traceback())

# import werkzeug
# from frappe.utils import redirect

@frappe.whitelist(allow_guest=True)
def erplogout():
	try:
		# frappe.session.destroy()
		user = frappe.session.user
		frappe.local.login_manager.logout()
		# logOut = requests.get(url = frappe.utils.get_url()+"/api/method/logout")
		frappe.db.commit()
		from frappe.sessions import clear_sessions
		clear_sessions(user=user, keep_current=True, force=True)
		return "Success"
	except Exception:
		frappe.log_error("erplogout",frappe.get_traceback())