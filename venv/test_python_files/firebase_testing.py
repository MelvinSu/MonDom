from flask_login import UserMixin
import pyrebase

firebaseConfig = {
    "apiKey": "os.environ['FIREBASE_API_KEY']",
    "authDomain": "mondom-97740.firebaseapp.com",
    "databaseURL": "https://mondom-97740.firebaseio.com",
    "projectId": "mondom-97740",
    "storageBucket": "mondom-97740.appspot.com",
    "messagingSenderId": "877143682729",
    "appId": "1:877143682729:web:54f672e485632c73ad43b8",
    "measurementId": "G-6S2J42P9KP"
};

firebase = pyrebase.initialize_app(firebaseConfig)

"""data = {
            "name": "Waffle",
            "email": "Iron"
        }
firebase = firebase.database()
firebase.child("users").child("0").set(data)
"""
# firebase.push(r.json()) <-- SAMPLE

temp_list = []
the_user = firebase.database().child("users").child("106141010986049248632").child("recent_searched_websites").get()
if (the_user.val() != None):
    for entry in the_user.each():
        temp_list.append(entry.val())
print(temp_list)
print (list(reversed(temp_list)))
