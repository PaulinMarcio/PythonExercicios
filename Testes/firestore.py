import requests
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# API_KEY = 'AIzaSyAoWF9e6mI-2Piz5WBxTHbuu2bGYKyu7_w'
# url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=' + API_KEY
# data = {"email": 'paulin.marcio@outlook.com', "password": 'Haineko33', "returnSecureToken": True}
# res = requests.post(url, data)
# id_token = res.json().get("idToken")

def get_auth():
    credentials = service_account.Credentials.from_service_account_file(
        "C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test2.json", 
        scopes=["https://www.googleapis.com/auth/datastore"], 
        subject="security@warren.com.br",
        )
    return AuthorizedSession(credentials)

def get_users(auth):
    base_url = "https://firestore.googleapis.com"
    url = base_url + "/v1/projects/fir-test-automation/databases"

    res = auth.get(url)
    res_body = res.json()
    print(res_body)

get_users(get_auth())