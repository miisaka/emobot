import os
from flask import Flask, send_file, jsonify, request,  abort, json, session
import app.db as db
import twillio

app = Flask(__name__)

app.secret_key = 'nathanChao'

@app.route("/hello")
def hello():
    return jsonify({
        'data': 'hello world!'
    })
@app.route("/")
def main():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)

@app.route("/register", methods=['POST'])
def register():
    username = (request.json['username'])
    password = (request.json['password'])
    contactName = (request.json['contactName'])
    contactNumber = (request.json['contactNumber'])
    relationToContact = (request.json['relationshipToContact'])
    db.insert_into_users(username, password, contactName, contactNumber, relationToContact)
    return json.dumps(request.json)

@app.route("/login", methods=['POST'])
def login():
    # if the user exists (?)
    print (request.json)
    username = (request.json['username'])
    password = (request.json['password'])
    print ('username is ' + username)
    print ('password is ' + password)
    if(db.query_users(username) == password):
        session['username'] = username
        print('horray everythings right')
    return json.dumps(request.json)

@app.route("/chat", methods=['POST'])
def chat():
    print request.json
    return jsonify({
        'message': 'hello world!'
    })


# Everything not declared before (not a Flask route / API endpoint)...
@app.route('/<path:path>')
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)


if __name__ == "__main__":
    db.create_tables()
    # Only for debugging while developing
    # db.insert_into_users('user1','pw1','contact1', 1234, 'papa')
    db.query_users_info('user1')
    # twillio.send_sms("Georgio", "15144653168", "papa", "angry")
    app.run(host='0.0.0.0', port=80)
    db.close_connection()

