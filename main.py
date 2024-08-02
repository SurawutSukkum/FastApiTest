from fastapi import FastAPI
import uvicorn 
import threading
from datetime import datetime
app = FastAPI()

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

@app.get("/StationName")
async def fetch_StationName():
    return '{"StationName":"'"StationName"+str(Time)+'"}'

@app.get("/Status")
async def fetch_Status():
    return '{"Status":"'"Status"+str(Time)+'"}'

@app.get("/Model")
async def fetch_Model():
    return '{"Model":"'"Model"+str(Time)+'"}'

@app.get("/CycleTime")
async def fetch_CycleTime():
    return '{"CycleTime":"'"CycleTime"+str(Time)+'"}'

@app.get("/Count")
async def fetch_Count():
    return '{"Count":"'"Count"+str(Time)+'"}'

@app.get("/OEE")
async def fetch_OEE():
    return '{"OEE":"'"OEE"+str(Time)+'"}'

@app.get("/YIELD")
async def fetch_YIELD():
    return '{"YIELD":"'"YIELD"+str(Time)+'"}'

@app.get("/RunTime")
async def fetch_RunTime():
    return '{"RunTime":"'"RunTime"+str(Time)+'"}'

@app.get("/DownTime")
async def fetch_DownTime():
    return '{"DownTime":"'"DownTime"+str(Time)+'"}'

@app.get("/IdleTime")
async def fetch_IdleTime():
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
    uvicorn.run("main:app", host = '127.0.0.1', port = 8080, reload = True, debug = True)