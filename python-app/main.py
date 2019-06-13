import json
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Home Page!'

@app.route('/looqers')
def get_looqers():
    req = request.get_json()
    looqers = requests.get('http://node-app:3000')
    var = json.loads(looqers.content.decode('utf-8'))
    return var[0]

app.run(host='0.0.0.0')
