import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore as fr
from firebase_admin import db

cred = credentials.Certificate("./serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://altintas-sigorta-default-rtdb.firebaseio.com/'})

firestore = fr.client()
database = db
