import os
import pprint
from termcolor import colored

pp = pprint.PrettyPrinter(indent=4)
ppfiles = pprint.PrettyPrinter(indent=4)

#  Open file and read it in line by line
with open('/Users/bnolte/listdir/list.txt') as f:
  directories = f.readlines()

# For each line (directory) list the contents of the dir
for subdir in directories:
  dircontents =  os.listdir(subdir.rstrip())
  print colored(subdir)
  pp.pprint(dircontents)

