import json
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


def get_auth():
    credentials = service_account.Credentials.from_service_account_file(
        "C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test2.json",
        scopes=[
            "https://www.googleapis.com/auth/datastore",
            "https://www.googleapis.com/auth/identitytoolkit",
        ],
        subject="firebase-adminsdk-vgoh3@fir-test-automation.iam.gserviceaccount.com",
    )
    return AuthorizedSession(credentials)


def coll_req(auth, base_url, project, coll_name):
    coll_data = []
    url = base_url + f"/v1/projects/{project}/databases/(default)/documents/{coll_name}"
    res = auth.get(url)
    res_body = res.json()
    for user in res_body["documents"]:
        coll_data.append(user)
    return coll_data


def get_users(auth):
    base_url = "https://firestore.googleapis.com"
    project = "fir-test-automation"

    coll_users = coll_req(auth, base_url, project, "users")
    coll_groups = coll_req(auth, base_url, project, "groups")
    coll_roles = coll_req(auth, base_url, project, "roles")
    coll_auth = coll_req(auth, base_url, project, "authorization")

    # uid = []
    # for id in coll_users:
    #     user_id = id["name"]
    #     user_id = user_id[-28:]
    #     user_id_json = json.dumps(user_id)
    #     user_id_json = user_id_json[1:-1]
    #     uid.append(user_id_json)

    # body = {"localId": uid}
    # email = auth.post(f"https://identitytoolkit.googleapis.com/v1/accounts:lookup", body)
    # email_json = email.json()
    # emails = []
    # for user_email in email_json["users"]:
    #     emails.append(user_email["email"])

    # print(json.dumps(emails, indent=4))
    # print(json.dumps(coll_users, indent=4))
    # print(json.dumps(coll_groups, indent=4))
    # print(json.dumps(coll_roles, indent=4))
    # print(json.dumps(coll_auth, indent=4))

    for user in coll_users:
        groups = []
        roles = []
        authentications = []
        full_user = {
            "id": "",
            "email": "",
            "groups": [
                {
                    "group_id": "",
                    "group_roles": [{"role_id": "", "role_authentications": []}],
                }
            ],
        }
        id = "" 
        id = user["name"]
        id = id[-28:]
        id = json.dumps(id)
        id = id[1:-1]
        body = {"localId": id}
        
        email = auth.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:lookup", body
        )
        email = email.json()


        for group in user["fields"]["groups"]["arrayValue"]["values"]:
            group_id = group["referenceValue"]
            group_id = json.dumps(group_id)
            group_id = group_id[1:-1]
            index = group_id.rindex("/") + 1
            group_id = group_id[index:]
            groups.append(group_id)
            for group_role in coll_groups:
                if group_id == group_role["name"]:
                
                    
        

        full_user["id"] = id
        full_user["email"] = email["users"][0]["email"]
        full_user["groups"] = groups
        print(full_user)


get_users(get_auth())
