from flask import Flask, request
import json
import watsonTest

app = Flask(__name__)

@app.route('/watsonTest', methods=['POST'])
def input_chat():
    input = request.body['message']
    response = watsonTest.conversationInput(input)

    return response
