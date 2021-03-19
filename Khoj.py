import params as params
import pyrebase
from flask import Flask, render_template, request
import smtplib
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
firebase=pyrebase.initialize_app(config)
db=firebase.database()
#comments added
#hfhfhfhhfhf

def mail_func(rec,msg):
    sender = "khoj.alerts@gmail.com"
    password = "Khoj@123"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, rec, msg)
    print("done")


@app.route("/",methods=['GET','POST'])
def print4():

    if request.method=='POST':
             data2 = {
                 "Email": request.form.get('email'),
                 "MobileNo": request.form.get('MobileNo'), "DOB": request.form.get('dateofbirth'),
                 "State": request.form.get('State'), "City": request.form.get('City'),
                 "Pincode": request.form.get('Pincode'),"Gender":request.form.get('optradio'),
                 "Age": request.form.get('Age'), "Height": request.form.get('Height'),
                 "Description": request.form.get('Description')
                 }
             db.child("Alert").child(str(request.form.get('fname'))).set(data2)
             mail_func(request.form.get('email'),(request.form.get('fname') + "\n" + request.form.get('MobileNo') +"\n" + request.form.get('State') + "\n" +request.form.get('optradio')))
    return render_template('index.html', params=params)




app.run(debug=True)
# mysqlclient @ file:///C:/Users/LENOVO/Downloads/mysqlclient-1.4.6-cp39-cp39-win_amd64.whl