import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app with credentials
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
firebase_admin.initialize_app(cred)

# Get the Firestore client
db = firestore.client()
