from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hey, it's working"

@app.route('/home')
def home1():
    return "CI/CD pipeline"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
