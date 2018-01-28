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
    return jsonify({
        'data': 'hello world!'
    })
    # print(db.query_users(request.form['username']))
    # print(request.form['username'])
    # return(request.form['username'])