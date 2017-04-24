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
#client.mongodirectorylist
pp = pprint.PrettyPrinter(indent=4)
collection = client.mongodirectorylist.mongocollection


with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

for files in directories:
  dircontents =  os.listdir(files.rstrip())


json_string = json.dumps(dircontents)

print json_string
print collection
print client.mongodirectorylist



#need to get dircontents into map format
#result = client.mongodirectorylist.mongocollection.insert_many(dircontents)
