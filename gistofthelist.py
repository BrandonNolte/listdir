import os
import sys
import pprint
import json
import pymongo
from pymongo import MongoClient
from bson import BSON
from bson import json_util

client_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(client_uri)
db = client['mongodirectorylist']
#client.mongodirectorylist
pp = pprint.PrettyPrinter(indent=4)
collection = client.mongodirectorylist.mongocollection


with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

for x in directories:
  filelist =  os.listdir(x.rstrip())
  formattedfiles = {"File": (filelist)}

sys.exit()  



#print formattedfiles

post = collection.insert_one(formattedfiles)
#print collection.find()
print post.inserted_id
pprint.pprint(collection.find_one({"_id": post.inserted_id})) 

#collectioninsert = collection.(json_string)




#print collection


#need to get dircontents into map format
#result = client.mongodirectorylist.mongocollection.insert_many(dircontents)
