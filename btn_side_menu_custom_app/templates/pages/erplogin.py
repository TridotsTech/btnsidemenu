import frappe ,requests, json
from frappe import _

def get_context():
    userId = frappe.form_dict.userId
    login_erp(userId)

@frappe.whitelist()
def login_erp(userId):
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
            frappe.log_error("jsonnnn",json)
            if userCredJSON['data']:
                frappe.local.login_manager.authenticate(userCredJSON['data'][0].get('userName'), userCredJSON['data'][0].get('password'))
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

import werkzeug
# from frappe.utils import redirect
@frappe.whitelist(allow_guest=True)
def erplogout():
    try:
        frappe.session.destroy()
        frappe.local.login_manager.logout()
        return "Success"
    except Exception:
        frappe.log_error("erplogout",frappe.get_traceback())