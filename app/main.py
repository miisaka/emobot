import os
import app.db as db


from flask import Flask, send_file, jsonify, request,  abort, json

app = Flask(__name__)

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
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)
    # db.insert_into_users("all params into here")

@app.route("/login", methods=['POST'])
def login():
    # if the user exists (?)
    print (request.json)
    username = (request.json['username'])
    password = (request.json['password'])
    print ('username is ' + username)
    print ('password is ' + password)
    if(db.query_users(username) == password):
        print('horray everythings right')
    return json.dumps(request.json)


    # print(request.form['username'])
    # return(request.form['username'])

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
    app.run(host='0.0.0.0', port=80)
    db.close_connection()

