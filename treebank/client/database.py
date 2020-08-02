import os

from pymongo import MongoClient


MONGODB_SERVER_HOST = os.getenv('MONGODB_SERVER_HOST', 'localhost')
MONGODB_SERVER_PORT = os.getenv('MONGODB_SERVER_PORT', '27017')

client = MongoClient(MONGODB_SERVER_HOST, int(MONGODB_SERVER_PORT))
db = client.treebank
