import os
import sys
import pprint
import json
import pymongo
import time
from pymongo import MongoClient
from bson import BSON
from bson import json_util

client_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(client_uri)
db = client['mongodirectorylist']
#client.mongodirectorylist
pp = pprint.PrettyPrinter(indent=4)

newcollection = time.time()
collectionstr = str(newcollection)
collection = client.mongodirectorylist[collectionstr]


with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

for directory in directories:
  strippeddir = directory.rstrip()
  filelist =  os.listdir(strippeddir)
  formattedfiles = {"directory":strippeddir, "file":filelist}
  post = collection.insert_one(formattedfiles)
  pprint.pprint(collection.find_one({"_id": post.inserted_id})) 
  print "objectid=" + str(post.inserted_id)
print(collection)  

sys.exit()  


