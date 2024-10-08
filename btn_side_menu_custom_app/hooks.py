from . import __version__ as app_version

app_name = "btn_side_menu_custom_app"
app_title = "Btn Side Menu Custom App"
app_publisher = "tridotstech"
app_description = "Btn Side Menu Custom App"
app_email = "info@tridotstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["https://fonts.googleapis.com/css2?family=Poppins:wght@200;400;500;600&display=swap","/assets/btn_side_menu_custom_app/css/frappe_side_menu.css","/assets/btn_side_menu_custom_app/css/ui-icons-regular.css"]
app_include_js = ["/assets/btn_side_menu_custom_app/js/frappe_side_menu.js","/assets/btn_side_menu_custom_app/js/jquery.slimscroll.js"]

on_session_creation  = "btn_side_menu_custom_app.btn_side_menu_custom_app.api.set_default_route"

# include js, css files in header of web template
# web_include_css = "/assets/btn_side_menu_custom_app/css/btn_side_menu_custom_app.css"
# web_include_js = "/assets/btn_side_menu_custom_app/js/btn_side_menu_custom_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "btn_side_menu_custom_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "btn_side_menu_custom_app.utils.jinja_methods",
#	"filters": "btn_side_menu_custom_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "btn_side_menu_custom_app.install.before_install"
# after_install = "btn_side_menu_custom_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "btn_side_menu_custom_app.uninstall.before_uninstall"
# after_uninstall = "btn_side_menu_custom_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "btn_side_menu_custom_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"btn_side_menu_custom_app.tasks.all"
#	],
#	"daily": [
#		"btn_side_menu_custom_app.tasks.daily"
#	],
#	"hourly": [
#		"btn_side_menu_custom_app.tasks.hourly"
#	],
#	"weekly": [
#		"btn_side_menu_custom_app.tasks.weekly"
#	],
#	"monthly": [
#		"btn_side_menu_custom_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "btn_side_menu_custom_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "btn_side_menu_custom_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "btn_side_menu_custom_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["btn_side_menu_custom_app.utils.before_request"]
# after_request = ["btn_side_menu_custom_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["btn_side_menu_custom_app.utils.before_job"]
# after_job = ["btn_side_menu_custom_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"btn_side_menu_custom_app.auth.validate"
# ]

