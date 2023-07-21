import requests, json
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
# url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=' + API_KEY
# data = {"email": 'paulin.marcio@outlook.com', "password": 'Haineko33', "returnSecureToken": True}
# res = requests.post(url, data)
# id_token = res.json().get("idToken")

def get_auth():

    credentials = service_account.Credentials.from_service_account_file(
        "C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test2.json", 
        scopes=["https://www.googleapis.com/auth/datastore"], 
        subject="firebase-adminsdk-vgoh3@fir-test-automation.iam.gserviceaccount.com",
        )
    return AuthorizedSession(credentials)

	

def get_users(auth):
    users = []
    base_url = "https://firestore.googleapis.com"
    url = base_url + "/v1/projects/fir-test-automation/databases/(default)/documents/users"

    res = auth.get(url)
    res_body = res.json()
    for user in res_body["documents"]:
        email = user["name"]
        email = email[65:]
        users.append(email)
    print(users)

    url_email = "https://identitytoolkit.googleapis.com/v1/accounts:lookup"
    for email in users:
        res = requests.post(url_email, data=email)
        res_body = res.json()
        print(res.json())

get_users(get_auth())