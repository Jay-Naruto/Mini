import params as params
import pyrebase
from flask import Flask, render_template, request
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
v1="jay"
users = db.child("Users").order_by_child("Mobile").get()
if v1 == users.each():
    print('correct')
