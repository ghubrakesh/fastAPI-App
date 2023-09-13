import os
from dotenv import load_dotenv
load_dotenv('MONGO_URI')

URI = os.getenv('MONGO_URI')
from pymongo import MongoClient
conn = MongoClient(URI)