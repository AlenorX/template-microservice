from fastapi import FastAPI, Body
from utilities import Utilities
from yaml_config import YamlUtilities

app = FastAPI()
utility = Utilities()
manager = YamlUtilities("yaml/endpoints.yml")
source = manager.deserializer()
endpoints = source["endpoints"]


@app.get(endpoints["status"])
def status():
    return {"status": True, "message": "Microservice is alive"}

@app.get(endpoints["root"])
def root():
    return {"message": "Hello, World!"}