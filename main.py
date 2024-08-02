from fastapi import FastAPI
import uvicorn 

app = FastAPI()

MOVIES_LIST = [{"name" : "TENET"}]

@app.get("/movies")
async def fetch_movies():
    return {"data" : MOVIES_LIST}

#http://127.0.0.1:8080/movies
if __name__ == "__main__":
    uvicorn.run("main:app", host = '127.0.0.1', port = 8080, reload = True, debug = True)