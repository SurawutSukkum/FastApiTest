from fastapi import FastAPI
import uvicorn 
import threading
from datetime import datetime
app = FastAPI()

MOVIES_LIST = [{" " : " "}]

@app.get("/movies")
async def fetch_movies():
    return {"data" : MOVIES_LIST}

def mqtt_thread():
    global MOVIES_LIST 
    while True:
          t = datetime.fromtimestamp(datetime.timestamp(datetime.now())).strftime("%Y-%m-%d-%H:%M:%S")
          MOVIES_LIST = [{"name" : str(t)}]
def serial_thread():
    print("start") 
mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.start()
serial_thread = threading.Thread(target=serial_thread)
serial_thread.start()
#http://127.0.0.1:8080/movies
if __name__ == "__main__":
    uvicorn.run("main:app", host = '127.0.0.1', port = 8080, reload = True, debug = True)