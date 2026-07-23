import fastapi
import uvicorn

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Lets build a Calculator API using Fast API"}

@app.get("/calculate")

async def calculate(a: int, b: int, operation: str):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return {"error": "Division by zero is not allowed."}
        result = a / b
    else:
        return {"error": "Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."}

    return {"result": result}   
  




