import requests
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/firebase.readonly']
SERVICE_ACCOUNT_FILE = 'C:/Users/marcio.paulin_warren/Documents/GitHub/Python/PythonExercicios/Testes/fir-test.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
firebase = googleapiclient.discovery.build('firestore','v1beta1', credentials=credentials)

print(credentials)