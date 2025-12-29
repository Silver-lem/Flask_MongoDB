from flask import Flask

app = Flask(__name__) #An instance of flask class

@app.route("/")
def home():
    return "<h1>Hello World</h1>"