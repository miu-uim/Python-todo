from flask import Flask

app = Flask(__name__)

@app.route('/def')
def hello_world():
    message = "Hello World"
    return message