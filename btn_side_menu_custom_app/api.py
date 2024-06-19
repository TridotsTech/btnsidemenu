import frappe,requests
from keycloak import KeycloakOpenID,KeycloakAdmin,KeycloakOpenIDConnection

@frappe.whitelist(allow_guest=True)
def test_loggin(usr,pwd):
    try:
        keycloak_openid = KeycloakOpenID(server_url="https://pauth.propixtech.com/auth",
                                    client_id="TASMAC_FINANCE",
                                    realm_name="TASMAC",
                                    client_secret_key="LnRJZPFETs619zk6zuEjHhnMIELsTsRo")

        token = keycloak_openid.token(usr,pwd)

        frappe.clear_cache(usr)
        from frappe.sessions import clear_sessions
        clear_sessions(user=usr, keep_current=True, force=True)
        # frappe.local.login_manager.user = usr
        frappe.local.login_manager.authenticate(usr, pwd)
        frappe.local.login_manager.post_login()
    except:
        frappe.throw(title="Error",msg="Invalid Login Credentials")





@frappe.whitelist(allow_guest=True)
def login_via_keycloak():
    keycloak_openid = KeycloakOpenID(server_url="https://pauth.propixtech.com/auth",
                                 client_id="TASMAC_FINANCE",
                                 realm_name="TASMAC",
                                 client_secret_key="LnRJZPFETs619zk6zuEjHhnMIELsTsRo")
    token = keycloak_openid.token("User_Section_B","Tasmac@123")
    access_token = token['access_token']



@frappe.whitelist(allow_guest=True)
def get_admin_access_token():
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJNYjhuY2t6ZHoxVlFXMlcyOVE0cElfNmcyWmZzLUR0Tng3aEJlZjcyaWFzIn0.eyJleHAiOjE3MTMxNzk4NjIsImlhdCI6MTcxMzE3OTU2MiwianRpIjoiODFlMmI5MzMtYjJjOS00Njg5LWJhOTgtNTM2MGU5ZTc1NTNhIiwiaXNzIjoiaHR0cHM6Ly9wYXV0aC5wcm9waXh0ZWNoLmNvbS9yZWFsbXMvVEFTTUFDIiwiYXVkIjpbInJlYWxtLW1hbmFnZW1lbnQiLCJUQVNNQUNfSFJNUyIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiOTA2ZjM4NTctZDBkZS00NGYzLWI2NWItYTk0NDEzYjIzYWFjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiVEFTTUFDLVNDTSIsInNlc3Npb25fc3RhdGUiOiI5MzhmNjFjZi02ZGQzLTQ2MzktOTk3Mi05NTE1NGU5ZjQ3OGYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vcWEuZXhjaXNlLnByb3BpeHRlY2guY29tIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwiZGVmYXVsdC1yb2xlcy10YXNtYWMiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiVEFTTUFDLVNDTSI6eyJyb2xlcyI6WyJ1bWFfcHJvdGVjdGlvbiIsImFkbWluIl19LCJUQVNNQUNfSFJNUyI6eyJyb2xlcyI6WyJ1bWFfcHJvdGVjdGlvbiJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJkZWxldGUtYWNjb3VudCIsIm1hbmFnZS1jb25zZW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIHN1cHBsaWVyX2NsaWVudF9zY29wZSBlbWFpbCIsInNpZCI6IjkzOGY2MWNmLTZkZDMtNDYzOS05OTcyLTk1MTU0ZTlmNDc4ZiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6IlJvaGl0IEFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicm9oaXRfYWRtaW4iLCJnaXZlbl9uYW1lIjoiUm9oaXQiLCJmYW1pbHlfbmFtZSI6IkFkbWluIiwiZW1haWwiOiJyb2hpdF9lc29AcHJvcGl4dGVjaC5jb20ifQ.hjQqKpI2xf4Ed8439ZcrBAx3ydyLr6iUmpgrnZNDBsnHTiKGl6Zat6vrPkYYy8pgoWhZ1ezLgqQA-8u5_5YnSQRKH6oZZAHg88X8QrB6-sIngfbWo4o3YQbWYwKLv8bfJEiTu1nF7SA5vdl_gOmc2mXOneck5WYgS3rP9qpIqCWl3hF6ZEew6dhpnK9WVjoVdqpmT1-jgKvpgeS5a0I2z3JHeF64z-m1OmC-4a2beGGOF4ItGHg7UrudIDEA-ThtVYVGFPhto_wYiSAu7_kJP3ACxUEiM5hfoxjN2u2WkDa9782XudUSaIMUTZU_DXRJk0c1ktq-mf2lMpHvszEW3w"

    url = "https://pauth.propixtech.com/realms/TASMAC/protocol/openid-connect/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept":"*/*",
        "X-API-Key": api_key,
    }

    data = {
        "grant_type": "password",
        "client_id": "TASMAC_FINANCE",
        "client_secret": "LnRJZPFETs619zk6zuEjHhnMIELsTsRo",
        "username": "tasmac_admin",
        "password": "Tasmac@123",
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response_data = response.json()
        return response_data['access_token']

    except requests.exceptions.RequestException as e:
        return f"{e}"

@frappe.whitelist()
def authorize_user_with_keycloak():
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJNYjhuY2t6ZHoxVlFXMlcyOVE0cElfNmcyWmZzLUR0Tng3aEJlZjcyaWFzIn0.eyJleHAiOjE3MTMxNzk4NjIsImlhdCI6MTcxMzE3OTU2MiwianRpIjoiODFlMmI5MzMtYjJjOS00Njg5LWJhOTgtNTM2MGU5ZTc1NTNhIiwiaXNzIjoiaHR0cHM6Ly9wYXV0aC5wcm9waXh0ZWNoLmNvbS9yZWFsbXMvVEFTTUFDIiwiYXVkIjpbInJlYWxtLW1hbmFnZW1lbnQiLCJUQVNNQUNfSFJNUyIsImJyb2tlciIsImFjY291bnQiXSwic3ViIjoiOTA2ZjM4NTctZDBkZS00NGYzLWI2NWItYTk0NDEzYjIzYWFjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiVEFTTUFDLVNDTSIsInNlc3Npb25fc3RhdGUiOiI5MzhmNjFjZi02ZGQzLTQ2MzktOTk3Mi05NTE1NGU5ZjQ3OGYiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHBzOi8vcWEuZXhjaXNlLnByb3BpeHRlY2guY29tIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImFkbWluIiwiZGVmYXVsdC1yb2xlcy10YXNtYWMiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiVEFTTUFDLVNDTSI6eyJyb2xlcyI6WyJ1bWFfcHJvdGVjdGlvbiIsImFkbWluIl19LCJUQVNNQUNfSFJNUyI6eyJyb2xlcyI6WyJ1bWFfcHJvdGVjdGlvbiJdfSwiYnJva2VyIjp7InJvbGVzIjpbInJlYWQtdG9rZW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJ2aWV3LWFwcGxpY2F0aW9ucyIsInZpZXctY29uc2VudCIsInZpZXctZ3JvdXBzIiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJkZWxldGUtYWNjb3VudCIsIm1hbmFnZS1jb25zZW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIHN1cHBsaWVyX2NsaWVudF9zY29wZSBlbWFpbCIsInNpZCI6IjkzOGY2MWNmLTZkZDMtNDYzOS05OTcyLTk1MTU0ZTlmNDc4ZiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6IlJvaGl0IEFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicm9oaXRfYWRtaW4iLCJnaXZlbl9uYW1lIjoiUm9oaXQiLCJmYW1pbHlfbmFtZSI6IkFkbWluIiwiZW1haWwiOiJyb2hpdF9lc29AcHJvcGl4dGVjaC5jb20ifQ.hjQqKpI2xf4Ed8439ZcrBAx3ydyLr6iUmpgrnZNDBsnHTiKGl6Zat6vrPkYYy8pgoWhZ1ezLgqQA-8u5_5YnSQRKH6oZZAHg88X8QrB6-sIngfbWo4o3YQbWYwKLv8bfJEiTu1nF7SA5vdl_gOmc2mXOneck5WYgS3rP9qpIqCWl3hF6ZEew6dhpnK9WVjoVdqpmT1-jgKvpgeS5a0I2z3JHeF64z-m1OmC-4a2beGGOF4ItGHg7UrudIDEA-ThtVYVGFPhto_wYiSAu7_kJP3ACxUEiM5hfoxjN2u2WkDa9782XudUSaIMUTZU_DXRJk0c1ktq-mf2lMpHvszEW3w"

    url = "https://pauth.propixtech.com/admin/realms/TASMAC/protocol/openid-connect/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept":"*/*",
        "X-API-Key": api_key,
    }

    data = {
        "grant_type": "password",
        "client_id": "TASMAC_FINANCE",
        "client_secret": "LnRJZPFETs619zk6zuEjHhnMIELsTsRo",
        "username": "User_Section_B",
        "password": "Tasmac@123",
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response_data = response.json()
        return response_data

    except requests.exceptions.RequestException as e:
        return f"{e}"
    
@frappe.whitelist(allow_guest=True)
def get_role_mappings(admin_access_token):
    url = "https://pauth.propixtech.com/admin/realms/TASMAC/users/?username=User_Section_B"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization':f"Bearer {admin_access_token}"
    }
    data = {
        "grant_type": "password",
        "client_id": "TASMAC_FINANCE",
        "client_secret": "LnRJZPFETs619zk6zuEjHhnMIELsTsRo",
        "username": "User_Section_B",
        "password": "Tasmac@123",
    }

    try:
        response = requests.get(url,headers=headers,data=data)
        response.raise_for_status()
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        return f"{e}"

@frappe.whitelist(allow_guest=True)
def custom_login():
    admin_access_token = get_admin_access_token()
    user_authorized = authorize_user_with_keycloak()
    user_mapped_roles = get_role_mappings(admin_access_token)
    return user_mapped_roles
    

