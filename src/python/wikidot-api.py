import config
import os
import sys
import json
import itertools
import random
from datetime import datetime
from time import sleep
from xmlrpc.client import ServerProxy

#open file in working directory
if sys.platform.startswith('win'):
    __location__ = os.getcwd()
else:
    __location__ = os.path.normpath(os.getcwd() + os.sep + os.pardir)

filename = os.path.join(__location__ + "/src/json/revisions.json")
filename = os.path.normpath(filename)
print(filename)
json_fragment = {}
json_data = {}

#if file does not exist, write it
if os.path.exists(filename):
    append_write = "a"
else:
    append_write = "w"

#open JSON File
f = open(filename,append_write)
f.seek(0)
f.truncate()

#defining grouping function
def grouper(inputs, n):
    iters = [inputs[x:x+n] for x in range(0, len(inputs), n)]
    return iters

#calling wikidot API
s = ServerProxy('https://' + config.wikidot_username + ':' + config.wikidot_api_key + "@www.wikidot.com/xml-rpc-api.php")
pages = s.pages.select({"site": "scp-wiki"})

#calling grouping function
groups = grouper(pages, 10)
groups_len = len(groups)

#placing data into JSON file and active JSON string
for x in range(groups_len):
    mine = s.pages.get_meta({"site": "scp-wiki", "pages": groups[x]})
    json_fragment.update(mine)

#opening active JSON string
sorted_data = sorted(json_fragment, key=lambda x: json_fragment[x]['revisions'], reverse=True)
json_data = json.dumps(
    [json_fragment[x] 
        for x in sorted_data
    ], indent=3)
json_loaded = json.loads(json_data)


#writing active JSON string to file
f.write(json_data)
f.close()

#printing total number of collected pages
print("Total: " + str(len(json_fragment)))