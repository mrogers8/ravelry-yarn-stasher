from dotenv import load_dotenv
from fastapi import FastAPI
import json

from api.ravelry import ravelry_search_yarn, ravelry_get_yarn, ravelry_list_stash, ravelry_create_stash, ravelry_update_pack

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


#stash_id can also be "list"
@app.get("/stash/get/{stash_id}")
async def list_stash(stash_id: str):
    result = ravelry_list_stash(stash_id)
    return json.loads(result)


@app.get("/stash/create")
async def create_stash():
    result = ravelry_create_stash()
    stash_map = json.loads(result)
    print("STASH SUCCESSFUL: {fstash}".format(fstash=stash_map))

    return json.loads(ravelry_list_stash(stash_map['stash']['packs'][0]['stash_id']))
