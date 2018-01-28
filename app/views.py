from flask import Flask, request
import json
import watsonTest
import app.db as db

from flask import Flask, send_file
app = Flask(__name__)


@app.route("/register")
def register():
    db.insert_into_users("all params into here")

@app.route("/login")
def login():
    db.query_users("frontend username here")

@app.route('/watsonTest', methods=['POST'])
def input_chat():
    input = request.body['message']
    response = watsonTest.conversationInput(input)

    return response