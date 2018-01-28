import app.db as db

from flask import Flask, send_file
app = Flask(__name__)


@app.route("/register")
def register():
    db.insert_into_users("all params into here")

@app.route("/login")
def login():
    db.query_users("frontend username here")