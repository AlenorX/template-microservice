from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/status")
def status():
    return {"status": True, "message": "Microservice is alive"}

@app.get("/root")
def root():
    return {"message": "Hello, World!"}