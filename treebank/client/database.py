import os

from pymongo import MongoClient


MONGODB_SERVER_HOST = os.getenv('MONGODB_SERVER_HOST', 'localhost')


client = MongoClient(host=MONGODB_SERVER_HOST)
db = client.treebank
