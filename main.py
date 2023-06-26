from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()


@app.get("/get-users-by-company/{companyId}")
def index():

    client = MongoClient('mongodb://localhost:27017')
    db = client['users_app']
    collection = db['users']
    result = collection.find().where("id_comp").eq(1)
    
    for document in result:
        print(document)
    client.close()

    return {"Hello": "World"}
