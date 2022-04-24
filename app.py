from flask import Flask, jsonify, render_template, sessions, send_file
from flask import request
from flask_cors import CORS
from gevent import pywsgi
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def runit():
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    print("启动服务器")
    server.serve_forever()

if __name__ == '__main__':
    runit()
