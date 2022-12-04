import requests
import json
from flask import Flask, request
from flask_sock import Sock
from cryptography.fernet import Fernet

## So, this shit will use websocket & http shit
## And what it will do?
app = Flask(__name__)
sock = Sock(app)
SERVER_VERSION = "10B"

# Fuck, my left knee is hurts. Welp. I need to end this asap.

@app.route('/')
def main():
    return "TEST CHILLZONE SERVER"

@sock.route('/testers/JP-1')
def echo(ws):
    while True:
        data = ws.receive()
        print(data)
        if data == "Jikns":
            data = {
    "servername": "CHILL ZONE OFFICIAL",
    "serverver": f"{SERVER_VERSION}",
    "app_id": "0000000000000000",
    "admin": "NickSaltFoxu",
    "bpic": [
        "chill_zone",
        "chillmodee",
        "koisip"
    ],
    "spic": [
        "dev",
        "chill",
        "c_sharp",
        "python",
        "nodejs"
    ]
}
            print(f"Sent: {json.dumps(data)}")
            ws.send(json.dumps(data))
        else:
            ws.send(data + " = Server")

@sock.route('/testers/JP-1/reg')
def echo(ws):
    while True:
        data = ws.receive()
        print(data)
