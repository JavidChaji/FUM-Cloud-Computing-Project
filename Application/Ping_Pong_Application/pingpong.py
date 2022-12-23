from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Echo(BaseModel):
    echo: str

@app.get("/ping")
def ping():
    return {"Ping": "Pong"}
    
@app.post("/echo")
def echo(echo: Echo):
    return echo.echo
   