from random import randint

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

var = randint(100000, 999999)
email_first = ""


def mail_func(rec, msg):
    sender = "khoj.alerts@gmail.com"
    password = "Khoj@123"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, rec, msg)
    print("done")


@app.route("/first", methods=['GET', 'POST'])
def print0():
    if request.method == 'POST':
        try:
            global email_first
            mail_func(request.form.get('Verify'), str(var))
            email_first = str(request.form.get('Verify'))
            print(email_first)
            return render_template('OTP.html', params=params)
        except:
            return render_template('First.html', params=params)
    return render_template('First.html', params=params)


@app.route("/otp", methods=['GET', 'POST'])
def print1():
    if request.method == 'POST':
        if request.form.get('OTP') == str(var):
            return render_template('signup.html', params=params)
    return render_template('OTP.html', params=params)


@app.route("/signup", methods=['GET', 'POST'])
def print2():
    if request.method == 'POST':

        PA = str(request.form.get('Confirm'))
        data3 = {
            "FullName": request.form.get('FullName'),
            "Email": email_first,
            "Mobile": request.form.get('Mobile'),
            "Password": request.form.get('Confirm')
        }
        try:
            authe.create_user_with_email_and_password(email_first, PA)
            print("hdhdh")


            db.child("Users").child(str(request.form.get('FullName'))).set(data3)

        except:
            return render_template('signup.html', params=params)

    return render_template('signup.html', params=params)


@app.route("/", methods=['GET', 'POST'])
def print3():
    if request.method == 'POST':
        email_t = str(request.form.get('loginemail'))
        password_t = str(request.form.get('loginpass'))

        try:

            authe.sign_in_with_email_and_password(email_t, password_t)
            # print(xd)
            return render_template('index.html', params=params)
        except:
            return render_template('login.html', params=params)

    return render_template('login.html', params=params)


@app.route("/index", methods=['GET', 'POST'])
def print4():
    if request.method == 'POST':
        data2 = {
            "Email": request.form.get('email'),
            "MobileNo": request.form.get('MobileNo'), "DOB": request.form.get('dateofbirth'),
            "State": request.form.get('stt'), "City": request.form.get('stt2'),
            "Pincode": request.form.get('Pincode'), "Gender": request.form.get('optradio'),
            "Age": request.form.get('Age'), "Height": request.form.get('Height'),
            "Description": request.form.get('Description'),
            "Image": request.form.get('file')
        }
        try:
            db.child("Alert").child(str(request.form.get('fname'))).set(data2)
            mail_func(request.form.get('email'),
                      (request.form.get('fname') + "\n" + request.form.get('MobileNo') + "\n" + request.form.get(
                          'stt') + "\n" + request.form.get('optradio')))
        except:
            return render_template('Error.html', params=params)

    return render_template('index.html', params=params)


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(debug=True)
# mysqlclient @ file:///C:/Users/LENOVO/Downloads/mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
