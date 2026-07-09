from VectorDataBaseClass import *
from fastapi import FastAPI

vectorDB = vector_data_base('data/Product Information.json')
vectorDB.setupDataSetVariables()
vectorDB.setupCollection()

#Building the api:
app =  FastAPI()

@app.get("/")
def root():
    return {"Hello": "stupid"}

@app.get("/query")
def query(question: str):
    results = vectorDB.searchResults(question,2)
    return results