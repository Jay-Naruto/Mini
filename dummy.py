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
for user in users.each():
  if(user.val()['FullName']):
                    # fullname_d = user.val()['FullName']
                    # Age_d = user.val()['Age']
                    # Height_d = user.val()['Height']
                    # Pincode_d = user.val()['Pincode']
                    # Shop_m = user.val()['Shop Name']
                    lst.append({"FullName": user.val()['FullName'],
                                "Age": user.val()['Age'], "Pincode": user.val()['Pincode'],
                                })
  print(lst)


# for user in users.each():
#     print(user.val())