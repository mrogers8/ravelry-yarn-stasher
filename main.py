from dotenv import load_dotenv
from fastapi import FastAPI
import json

from api.ravelry import ravelry_search_yarn, ravelry_get_yarn

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/yarns/search/{query}")
async def search_yarn(query: str):
    result = ravelry_search_yarn(query)
    return json.loads(result)

@app.get("/yarns/get/{id}")
async def search_yarn(id: str):
    result = ravelry_get_yarn(id)
    return json.loads(result)
