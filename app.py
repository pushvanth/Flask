from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/places')
def places():
   return render_template('places.html')