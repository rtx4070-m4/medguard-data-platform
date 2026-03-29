
from fastapi import FastAPI
from pipeline.pipeline import Pipeline

app=FastAPI()

@app.get("/run-pipeline")
def run():
    p=Pipeline()
    return p.run()
