from pymongo import MongoClient
from pymongo.server_api import ServerApi
from env import username, password, cluster
from cats_db import cats 

client = MongoClient(
    f"mongodb+srv://{username}:{password}@{cluster}",
    server_api=ServerApi('1')
)
db = client.cats_hw3



db.cats.delete_many({})
db.cats.insert_many(cats)

print("... База успішно заповнена котами ...")