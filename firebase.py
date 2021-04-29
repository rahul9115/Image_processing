import pyrebase
import os
config={
    "apiKey": "AIzaSyAF-yR-zkh5M2SqayH4Iqa1Ncd4YOcG6bY",
    "authDomain": "meter-reading-c15ae.firebaseapp.com",
    "databaseURL": "https://meter-reading-c15ae-default-rtdb.firebaseio.com",
    "projectId": "meter-reading-c15ae",
    "storageBucket": "meter-reading-c15ae.appspot.com",
    "messagingSenderId": "832226172295",
    "appId": "1:832226172295:web:1c3588d6590ae357240722",
    "measurementId": "G-6TM2L3J7K2"
}
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
storage.child("meter.jpg").download(filename="meter1.jpg",path=os.path.basename("meter1.jpg"))