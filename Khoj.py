from random import randint
import os
import tempfile
import params as params
import pyrebase
from flask import Flask, render_template, request, flash
import smtplib

# hello
# hhn
from werkzeug.utils import secure_filename

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
storage = firebase.storage()

var = randint(100000, 999999)
email_first = ""
gmobile = ""
lst2 = []
fullname_m=''
Email_m=''
Mobile_m=''

email_t=""


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

        try:

            xd = authe.create_user_with_email_and_password(email_first, PA)
            print(xd)

            # return render_template('index.html', params=params)

            data3 = {
                "FullName": request.form.get('FullName'),
                "Email": email_first,
                "Mobile": request.form.get('Mobile'),
                "Password": request.form.get('Confirm'),
            }
            db.child("Users").child(str(request.form.get('Mobile'))).set(data3)
        except:
            return render_template('Error.html', params=params)

    return render_template('signup.html', params=params)


@app.route("/", methods=['GET', 'POST'])
def print3():
    if request.method == 'POST':
        lst = []
        lst3=[]
        global email_t
        global fullname_m
        global Email_m
        global Mobile_m

        email_t = str(request.form.get('loginemail'))
        password_t = str(request.form.get('loginpass'))

        try:

            authe.sign_in_with_email_and_password(email_t, password_t)
            # print(xd)
            users = db.child('Alert').order_by_child('FullName').get()
            profile = db.child('Users').order_by_child('FullName').get()
            for user in users.each():
                lst.append({"FullName": user.val()['FullName'],
                            "Age": user.val()['Age'],
                            "Height": user.val()['Height'],
                            "City": user.val()['City'],
                            "State": user.val()['State'],
                            "MobileNo": user.val()['MobileNo'],
                            "Image": user.val()['Image']
                            })
            for profile in profile.each():
                if (profile.val()['Email'] == email_t):
                    fullname_m = profile.val()['FullName']
                    Email_m = profile.val()['Email']
                    Mobile_m = profile.val()['Mobile']

            for records in users.each():
                if (records.val()['Email'] == email_t):
                    lst3.append({"FullName": records.val()['FullName'],
                                 "DOB": records.val()['DOB'],
                                 "City": records.val()['City'],

                                 })

            return render_template('index.html', params=params, lst=lst, lst3=lst3, fullname_m=fullname_m,
                                   Email_m=Email_m, Mobile_m=Mobile_m)
        except:
            return render_template('Error.html', params=params)

    return render_template('login.html', params=params)


@app.route("/index", methods=['GET', 'POST'])
def print4():
    if request.method == 'POST':
        global lst2
        lst3=[]
        f = request.files['file']
        f.save(f.filename)
        filename = secure_filename(f.filename)
        new_path = os.path.abspath(filename)
        print(new_path)
        storage.child(request.form.get('MobileNo')).put(f.filename)

        fileURL = storage.child(request.form.get('MobileNo')).get_url(None)
        data2 = {
            "FullName": request.form.get('fname'),
            "Email": request.form.get('email'),
            "MobileNo": request.form.get('MobileNo'), "DOB": request.form.get('dateofbirth'),
            "State": request.form.get('stt'), "City": request.form.get('stt2'),
            "Pincode": request.form.get('Pincode'), "Gender": request.form.get('optradio'),
            "Age": request.form.get('Age'), "Height": request.form.get('Height'),
            "Description": request.form.get('Description'),
            "Image": fileURL
        }
        try:




            db.child("Alert").child(str(request.form.get('MobileNo'))).set(data2)

            mail_func(request.form.get('email'),
                      (request.form.get('fname')
                       + "\n" + request.form.get('MobileNo')
                       + "\n" + request.form.get('stt')
                       + "\n" + request.form.get('optradio')))
            users = db.child('Alert').order_by_child('FullName').get()
            # profile = db.child('Users').order_by_child('FullName').get()

            for user in users.each():
                if (user.val()['FullName']):
                    lst2.append({"FullName": user.val()['FullName'],
                                 "Age": user.val()['Age'],
                                 "Height": user.val()['Height'],
                                 "City": user.val()['City'],
                                 "State": user.val()['State'],
                                 "MobileNo": user.val()['MobileNo'],
                                 "Image": user.val()['Image'],
                                 })

            for records in users.each():
                if (records.val()['Email'] == email_t):
                    lst3.append({"FullName": records.val()['FullName'],
                                 "DOB": records.val()['DOB'],
                                 "City": records.val()['City'],

                                 })
            # for profile in profile.each():
            #     if (profile.val()['Email'] == email_t):
            #         fullname_m = profile.val()['FullName']
            #         Email_m = profile.val()['Email']
            #         Mobile_m = profile.val()['Mobile']

            return render_template('index.html', params=params, lst=lst2,lst3=lst3, fileURL=fileURL,fullname_m=fullname_m ,Email_m=Email_m, Mobile_m=Mobile_m)
        except:
            return render_template('Error.html', params=params)

    return render_template('index.html', params=params)


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(debug=True)
# mysqlclient @ file:///C:/Users/LENOVO/Downloads/mysqlclient-1.4.6-cp39-cp39-win_amd64.whl


#  @message_api.route('/messenger/message/send/picture/individual', methods=['post'])
