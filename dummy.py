from random import randint
import os
import tempfile
import params as params
import pyrebase
from flask import Flask, render_template, request, flash
import smtplib

# hello
# hhn
app = Flask(__name__, template_folder='templates')

config = {
    "apiKey": "AIzaSyD8Uy9tJWNoRUEf7zo1212rD1cA20OKb80",
    "authDomain": "mars-c7bdc.firebaseapp.com",
    "databaseURL": "https://mars-c7bdc-default-rtdb.firebaseio.com",
    "projectId": "mars-c7bdc",
    "storageBucket": "mars-c7bdc.appspot.com",
    "messagingSenderId": "118583428832",
    "appId": "1:118583428832:web:7643daf17eb2de5d72b285",
    "measurementId": "G-9RK6Y1NT4L"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
authe = firebase.auth()
lst=[]
users = db.child('Alert').order_by_child('FullName').get()
for records in users.each():
    if (records.val()['Email'] == "jaynarutomistry@gmail.com"):
        lst.append({"FullName": records.val()['FullName'],
                     "DOB": records.val()['DOB'],
                     "City": records.val()['City'],
                     "Age": records.val()['Age'],
                     "Height": records.val()['Height'],

                     })
print(lst)


# for user in users.each():
#     print(user.val())