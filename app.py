from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "KubeSRE API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/incidents")
def incidents():

    with open("incidents.json", "r") as f:
        data = json.load(f)

    return data

@app.get("/analysis")
def analysis():

    with open("analysis_report.json", "r") as f:
        data = json.load(f)

    return data