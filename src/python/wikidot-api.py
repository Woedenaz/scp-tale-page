import config
import os
import sys
import json
import itertools
import random
from datetime import datetime
from time import sleep
from xmlrpc.client import ServerProxy

# Randomly select a time between 20 to 30 minutes
# before sleeping.
random_time_duration = random.randint(25,30)

# Randomly sleep between 60 to 120 seconds.
sleep_duration = random.randint(80,90)

# This is the start time of of loop used to track
# how much time has passed.
old_time = datetime.now()

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
    while True:
        # Check if the randomly selected duration has
        # passed before running your code block.
        if (datetime.now()-old_time).total_seconds() > random_time_duration:
            sleep(sleep_duration)

            # Reset all the time variables so the loop works
            # again.
            random_time_duration = random.randint(25,30)
            sleep_duration = random.randint(80,90)
            old_time = datetime.now()
            print("wait: " + str(sleep_duration))

        else:
            # Put your code in here.
            mine = s.pages.get_meta({"site": "scp-wiki", "pages": groups[x]})
            json_fragment.update(mine)
            print("wait: " + str(sleep_duration))
            pass

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