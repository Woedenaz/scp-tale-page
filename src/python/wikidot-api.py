import config
import os
import sys
import json
import itertools
import random
import datetime
from time import sleep, perf_counter
from xmlrpc.client import ServerProxy

#open file in working directory
__location__ = os.getcwd()

filename = os.path.join(__location__ + "/src/json/tales.json")
filename = os.path.normpath(filename)
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

fmt = "  Progress: {:>3}% estimated {} remaining"
start = perf_counter()

#calling wikidot API
s = ServerProxy('https://' + config.wikidot_username + ':' + config.wikidot_api_key + "@www.wikidot.com/xml-rpc-api.php")
pages = s.pages.select({"site": "scp-wiki", "tags_all": ["tale"]})
sleep(0.25)
totalpages = len(pages)
print("Total: " + str(totalpages))

#calling grouping function
groups = grouper(pages, 10)
totalgroups = len(groups)

num = len(groups)
start = perf_counter()
#placing data into JSON file and active JSON string
for x in range(len(groups)):
    #setting in-loop time
    pageinfo = s.pages.get_meta({"site": "scp-wiki", "pages": groups[x]})
    for y in pageinfo: 
        # Formatting Dates
        created = datetime.datetime.fromisoformat(pageinfo[y]["created_at"]).strftime("%Y-%m-%d %H:%M")
        pageinfo[y]["created_at"] = created
        updated = datetime.datetime.fromisoformat(pageinfo[y]["updated_at"]).strftime("%Y-%m-%d %H:%M")
        pageinfo[y]["updated_at"] = updated            

    # Be Nice
    sleep(0.25)

    # Progress %
    pagesleft = totalpages - len(pageinfo)
    os.system("cls" if os.name == "nt" else "clear")
    print("Page Groups Left: " + str(pagesleft))

    stop = perf_counter()
    remaining = round(((stop - start) * (num / (x + 1) - 1)))
    print(fmt.format(100 * x // num, str(datetime.timedelta(seconds=remaining))), end='\r')

    json_fragment.update(pageinfo)

# Remove Fragments
for x in list(json_fragment.keys()):
    if "fragment" in json_fragment[x]["fullname"]:
        del json_fragment[x]

#opening active JSON string
sorted_data = sorted(json_fragment, key=lambda x: json_fragment[x]['created_at'], reverse=True)
json_data = json.dumps(
    [json_fragment[x] 
        for x in sorted_data
    ], 
    indent=3,
    ensure_ascii=False)
json_loaded = json.loads(json_data)


#writing active JSON string to file
f.write(json_data)
f.close()

#printing total number of collected pages
print("Total Items: " + str(len(json_fragment)))