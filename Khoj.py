import params as params
from flask import Flask, render_template, request
import json
app = Flask(__name__, template_folder='templates')


@app.route("/")
def print1():
    return render_template('khojfront.html',params=params)
@app.route("/about")
def print2():
    return render_template('about.html',params=params)
@app.route("/newalerts")
def print3():
    return render_template('newalerts.html',params=params)
@app.route("/contact")
def print4():
    return render_template('contact.html',params=params)
@app.route("/viewallrecords")
def print5():
    return render_template('viewallrecords.html',params=params)

app.run(debug=True)
# mysqlclient @ file:///C:/Users/LENOVO/Downloads/mysqlclient-1.4.6-cp39-cp39-win_amd64.whl