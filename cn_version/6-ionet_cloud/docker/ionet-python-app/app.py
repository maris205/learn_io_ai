from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello from a Flask app running in an NVIDIA CUDA 13.0 container!"
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
