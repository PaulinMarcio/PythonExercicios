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

def renaming(name):
    name = json.dumps(name)
    name = name[1:-1]
    index = name.rindex("/") + 1
    name = name[index:]
    return name


def get_users(auth):
    base_url = "https://firestore.googleapis.com"
    project = "fir-test-automation"

    coll_users = coll_req(auth, base_url, project, "users")
    coll_groups = coll_req(auth, base_url, project, "groups")
    coll_roles = coll_req(auth, base_url, project, "roles")
    coll_auth = coll_req(auth, base_url, project, "authorization")

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

        #For para puxar os grupos dentro do usuário
        for group in user["fields"]["groups"]["arrayValue"]["values"]:
            group_dict = {}
            role_authentications = []
            group_id = group["referenceValue"]
            group_id = renaming(group_id)
            #For para puxar as roles dentro de cada grupo
            for group_role in coll_groups:
                group_name = group_role["name"]
                group_name = renaming(group_name)
                #If para comparar se o nome do grupo é o mesmo entre o grupo do usuário e o grupo da collection
                if group_id == group_name:
                    group_roles = []
                    i = 0
                    role_name = group_role["fields"]["roles"]["arrayValue"]["values"]
                    #Passando por todas as roles dentro de um grupo do usuário
                    while i < len(role_name):
                        role_dict = {}
                        role = role_name[i]["referenceValue"]
                        role = renaming(role)
                        role_dict["role_id"] = role
                        role_dict["role_authorizations"] = {}
                        i += 1
                        group_roles.append(role_dict)
                        for roles in coll_roles:
                            role = roles["name"]
                            role = renaming(role)
                            if role_name == role:
                                ...
            group_dict["group_id"] = group_id
            group_dict["group_roles"] = group_roles
            groups.append(group_dict)

        full_user["id"] = id
        full_user["email"] = email["users"][0]["email"]
        full_user["groups"] = groups
        print(json.dumps(full_user, indent=4))
    return full_user


get_users(get_auth())
