from flask import Flask, jsonify

app = Flask(__name__)

test_dictionary = {
    "name" : "test_dictionary"
}

@app.route('/')
def hello():
    return jsonify(test_dictionary)
