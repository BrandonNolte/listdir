import os
import pprint
import json
import pymongo
from pymongo import MongoClient
from bson import BSON
from bson import json_util
from termcolor import colored
client_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(client_uri)
db = client['mongodirectorylist']
client.mongodirectorylist

with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

for subdir in directories:
  dircontents =  os.listdir(subdir.rstrip())
  dircontents_parsed = json.dumps(dircontents)


#need to get dircontents into map format

result = client.mongodirectorylist.mongocollection.insert_many(dircontents)
