from dotenv import load_dotenv
from fastapi import FastAPI

from api.ravelry import get_yarn

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/yarns/search/")
async def search_yarn():
    return get_yarn()