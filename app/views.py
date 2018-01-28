from flask import Flask, request
import json
import watsonTest
import app.db as db

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/registerr", methods=['POST'])
def register():
    print(request.form['username'])
    return ''
    # db.insert_into_users("all params into here")

@app.route("/loginn", methods=['GET'])
def login():
<<<<<<< HEAD
    return jsonify({
        'data': 'hello world!'
    })
    # print(db.query_users(request.form['username']))
    # print(request.form['username'])
    # return(request.form['username'])
=======
    db.query_users("frontend username here")

@app.route('/watsonTest', methods=['POST'])
def input_chat():
    input = request.body['message']
    response = watsonTest.conversationInput(input)

    return response
>>>>>>> e55a6b46edad66bdc79dc34eb44e4db55307c86a
