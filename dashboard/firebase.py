import os
import firebase_admin
from firebase_admin import credentials, firestore

# Construye la ruta absoluta al archivo de credenciales
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtén el directorio de este archivo
cred_path = os.path.join(BASE_DIR, "datoschatbot-firebase-adminsdk-fbsvc-3192faeb5d.json")

# Inicializa Firebase con la ruta absoluta
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Conexión a Firestore
db = firestore.client()
