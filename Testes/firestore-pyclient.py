
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test2.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client(app)

docs_users = db.collection("users").stream()
docs_groups = db.collection("groups").stream()
docs_roles = db.collection("roles").stream()
docs_authorization = db.collection("authorization").stream()

print(docs_users, docs_groups, docs_roles, docs_authorization)
print('--------------------------')
print('--------------------------')

users = []

for doc in docs_users:
    users.append(doc.to_dict())

for doc in docs_groups:
    users.append(doc.to_dict())

for doc in docs_authorization:
    users.append(doc.to_dict())

for doc in docs_roles:
    users.append(doc.to_dict())


print(users)
print(id(users[0]['user3']))
print('--------------------------')
print('--------------------------')
page = auth.list_users()
print(page)
print('--------------------------')
print('--------------------------')

while page:
    for user in page.users:
        email = auth.get_user(user.uid)
        email = email.email
        print('User: ' + email)
    page = page.get_next_page()

    