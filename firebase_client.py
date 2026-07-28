import pyrebase

config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "disasterreliefportal.firebaseapp.com",
    "projectId": "disasterreliefportal",
    "storageBucket": "disasterreliefportal.firebasestorage.app",
    "messagingSenderId": "435080158100",
    "appId": "1:435080158100:web:a598fd2bee7de1b39e8d81",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()