import os
import pprint
import json
import pymongo
from bson import BSON
from bson import json_util
from termcolor import colored

def mongodb_connect(client_uri):
    try:
        return pymongo.MongoClient(client_uri)
    except pymongo.errors.connectionFailure:
         print "I have failed to connect to mongo {}".format(client_uri)


def insert_into_database(self):
    client_uri = "mongodb://localhost:27017"
    client = mongodb_connect(client_uri)
    db = client['mongodirectorylist']


#  Open file and read it in line by line
with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

# For each line (directory) list the contents of the dir
for subdir in directories:
  dircontents =  os.listdir(subdir.rstrip())
#  print colored(subdir, 'red')
  dircontents_parsed = json.dumps(dircontents)
#  print(dircontents_parsed)


print (mongodb_connect)
insert_into_database["mongodirectorylist"].insert(dircontents_parsed)
