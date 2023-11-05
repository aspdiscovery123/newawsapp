from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello AWS CI/CD application"  # Use the return statement to specify the response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
