from flask import Flask, request

app = Flask(__name__)

@app.route("/helloworld")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/login", methods=['POST'])
def login():
    email_address = request.form["email_address"]
    password = request.form["password"]
    print(f"Received {email_address} and {password}")
    return {"status": "SUCCESS"}

