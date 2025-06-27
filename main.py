# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Bark"}

@app.post("/speak")
async def speak():
    return {"audio": "base64 string here"}
