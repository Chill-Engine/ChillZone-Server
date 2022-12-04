import requests
import json
from flask import Flask, request
from flask_sock import Sock
import os
import sys
from pathlib import Path, PureWindowsPath 

clear = lambda: os.system('cls')

# You'll f**king laugh of this "future" function guys xDDDD
from cryptography.fernet import Fernet

## So, this shit will use websocket & http shit
## And what it will do?
app = Flask(__name__)
sock = Sock(app)
SERVER_VERSION = "10B"

# Paths
rootPath = PureWindowsPath(".\\CESData\\")
confPath = PureWindowsPath(".\\CESData\\configs\\")
confFPath = PureWindowsPath(".\\CESData\\configs\\serverConfig.json")
confPPath = PureWindowsPath(".\\CESData\\configs\\panelConfig.json")
keysPath = PureWindowsPath(".\\CESData\\keys\\")
ujsonPath = PureWindowsPath(".\\CESData\\users\\")

def pathor(folder):
    correct_path = Path(folder)
    return correct_path

def firstSetup():
    os.mkdir(f"{pathor(rootPath)}")
    os.mkdir(f"{pathor(confPath)}")
    tempF = open(f"{pathor(confFPath)}", "wt")
    tempF.write("""
    {
    "servername": "Your Server name",
    "serverver": "SERVER_VERSION", 
    "app_id": "Your Application ID from discord developers page",
    "admin": "you",
    "bpic": [
        "largepicture1",
        "largepicture2",
        "largepicture3"
    ],
    "spic": [
        "smallpicture1",
        "smallpicture2",
        "smallpicture3"
    ],
        "CCA": ["UA","RU","JP"],
        "NOR": 5
}
    """)
    tempF.close()
    tempF = open(f"{pathor(confPPath)}", "wt")
    tempF.write("""
    {
    "adminUsername": "YourUserName",
    "adminPassword": "YourPassWord"
}
    """)
    tempF.close()
    os.mkdir(f"{pathor(keysPath)}")
    os.mkdir(f"{pathor(ujsonPath)}")

if not os.path.exists(f"{pathor(rootPath)}"):
    print("Looks like you running ChillEngine Server for the first time...")
    firstSetup()
    print(f"Everything is ready! Configure {pathor(confFPath)} and restart server!")
    sys.exit(1)
else:
    pass

# Web stuff will be made after full end of suffering with websocket ._.

@app.route('/')
def main():
    return "TEST CHILLZONE SERVER"



@sock.route('/testers/<CountryCode>-<ServerNum>')
def tester(ws, CountryCode, ServerNum):
    while True:
        data = ws.receive()
        print(data)
        if data == "Jikns":
            data = json.load(f"{pathor(confFPath)}")
            print(f"Sent: {json.dumps(data)}")
            ws.send(json.dumps(data))
        else:
            ws.send(data + " = Server")

@sock.route('/testers/<CountryCode>-<ServerNum>/reg')
def reg(ws):
    while True:
        data = ws.receive()
        print(data)
