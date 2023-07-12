import firebase_admin
import json
from firebase_admin import db

# Conexão com o Firebase:

cred = firebase_admin.credentials.Certificate('C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test.json') # Credenciais em JSON
link = 'https://fir-test-automation-default-rtdb.firebaseio.com/' # Link da DB
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':link
	}) # Inicialização da DB

# Ações:

ref = db.reference("/Books/Best_Sellers/") # link/Books/Best_Sellers/

best_sellers = ref.get()
print(best_sellers)