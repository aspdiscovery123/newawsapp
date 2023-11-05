# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    "Hello AWS CI/CD application"

app.run(host='0.0.0.0',port=8080)
