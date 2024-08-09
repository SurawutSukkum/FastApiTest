from fastapi import FastAPI
import uvicorn 
import threading
from datetime import datetime
import json
from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # This will allow your React app to connect to this Flask API



StationName = 0
Status = 0
Model = 0
CycleTime = 0
Count = 0
OEE = 0
YIELD = 0 
RunTime = 0
DownTime = 0
IdleTime = 0
Time = 0 

@app.route('/data', methods=['GET'])
def get_data():
    # Simulate a data response
    return jsonify({"message": "StationName"+str(Time)})

@app.route('/StationName', methods=['GET'])
def fetch_StationName():
    return  jsonify({"StationName": "StationName"+str(Time)})


@app.route('/Status', methods=['GET'])
def fetch_Status():
    return '{"Status":"'"Status"+str(Time)+'"}'

@app.route('/Model', methods=['GET'])
def fetch_Model():
    data = {"name": "Jane Smith", "email": "janesmith@example.com", "job": "Data Scientist"}
    json_data = json.dumps(data)
    return  '{"Model":"'"Status"+str(Time)+'"}'

#'{"Model":"'"Model"+str(Time)+'"}'
#"{\"name\": \"Jane Smith\", \"email\": \"janesmith@example.com\", \"job\": \"Data Scientist\"}"

@app.route('/CycleTime', methods=['GET'])
def fetch_CycleTime():
    return '{"CycleTime":"'"CycleTime"+str(Time)+'"}'

@app.route('/Count', methods=['GET'])
def fetch_Count():
    return '{"Count":"'"Count"+str(Time)+'"}'

@app.route("/OEE", methods=['GET'])
def fetch_OEE():
    return '{"OEE":"'"OEE"+str(Time)+'"}'

@app.route("/YIELD", methods=['GET'])
def fetch_YIELD():
    return '{"YIELD":"'"YIELD"+str(Time)+'"}'

@app.route("/RunTime", methods=['GET'])
def fetch_RunTime():
    return '{"RunTime":"'"RunTime"+str(Time)+'"}'

@app.route("/DownTime", methods=['GET'])
def fetch_DownTime():
    return '{"DownTime":"'"DownTime"+str(Time)+'"}'

@app.route("/IdleTime", methods=['GET'])
def fetch_IdleTime():
    return '{"IdleTime":"'"IdleTime"+str(Time)+'"}'

def mqtt_thread():
    global Time
    while True:
          Time = datetime.fromtimestamp(datetime.timestamp(datetime.now())).strftime("%Y-%m-%d-%H:%M:%S")

def serial_thread():
    print("start") 

mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.start()
serial_thread = threading.Thread(target=serial_thread)
serial_thread.start()
#http://127.0.0.1:8080/StationName
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3001)