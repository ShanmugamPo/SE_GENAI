import fastapi
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Fast API Assignment"}

@app.get("/greet")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}
