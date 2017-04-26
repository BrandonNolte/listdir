import os
import pprint
import json
import pymongo
from pymongo import MongoClient
from bson import BSON
from bson import json_util
from termcolor import colored

#  Open file and read it in line by line
with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

# For each line (directory) list the contents of the dir
for subdir in directories:
  dircontents =  os.listdir(subdir.rstrip())
#  print colored(subdir, 'red')
  dircontents_parsed = json.dumps(dircontents)
#  print(dircontents_parsed)

def mongodb_connect(client_uri):
    try:
        return pymongo.MongoClient(client_uri)
    except pymongo.errors.connectionFailure:
         print "I have failed to connect to mongo {}".format(client_uri)
    return

def connect_to_database(dircontents_parsed):  #this is my keyword def
#    client_uri = mongodb_connect() 
    client_uri = "mongodb://localhost:27017"
#    client = mongodb_connect(client_uri)
    client = pymongo.MongoClient(client_uri)
    db = client['mongodirectorylist']
    print client #this should let me see if client and client uri are being called
    print pymongo.MongoClient.insert(dircontents_parsed)
    return



print mongodb_connect(client_uri = "mongodb://localhost:27017").connect_to_database(dircontents_parsed)
