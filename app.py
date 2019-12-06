from flask import Flask, jsonify
import os

app = Flask(__name__)

test_dictionary = {
    "name" : "test_dictionary"
}

@app.route('/')
def hello():
    return jsonify(test_dictionary)

@app.route('/api/v1/test_int/<int:test_int>')
def return_test_int(test_int):
    return f"<p>This is the int you specified: {test_int}</p>"

@app.route('/test_secret')
def return_secret():
    return os.environ['SECRET_TEST_VAR']
