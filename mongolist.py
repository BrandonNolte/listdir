import os
import sys
import pprint
import json
import pymongo
import time
from stat import *
from pymongo import MongoClient
from bson import BSON
from bson import json_util

client_uri = "mongodb://localhost:27017"

def mongodb_validate(client_uri):
    try:
        return pymongo.MongoClient(client_uri)
    except pymongo.errors.connectionFailure:
        print "I have failed to connect to mongo {}".format(client_uri)
    return

mongodb_validate( client_uri )
client = pymongo.MongoClient(client_uri)
db = client['mongodirectorylist']
newcollection = time.time()
collectionstr = str(newcollection)
collection = client.mongodirectorylist[collectionstr]

with open('/Users/bnolte/git/listdir/targets.txt') as f:
  directories = f.readlines()


for directory in directories:
  strippeddir = directory.rstrip()
  filelist =  os.listdir(strippeddir)
  joinedfile = str(strippeddir) + str(filelist) ## this join works but needs to be in a for loop to stat the file
  stringfile = str(joinedfile)
  statlist = os.lstat(stringfile)
  formattedfiles = {"directory":strippeddir, "file":filelist, "is_dir:":statlist} ### should this be in the for sub loop? 
  post = collection.insert_one(formattedfiles)
  pprint.pprint(collection.find_one({"_id": post.inserted_id})) 
  print "objectid=" + str(post.inserted_id)
print(collection)  

### next feature should be relationship building. Perhaps we could identify the diffrence between a file and a directory. I think it would be good goal to have a program that walks the entire directory structure. and is able to id each bit
#first story I will add file type mapping into the program giving it a field structure as fields
#second story should be to search for paths



sys.exit()  


