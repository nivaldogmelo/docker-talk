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
    looqers = requests.get('http://192.168.0.2:3000')
    amigos = json.loads(looqers.content)
    return amigos[0]

app.run(host='0.0.0.0')
