import os
import requests
import json
import string
import random
import re
from bs4 import BeautifulSoup
import pprint

#open file in working directory
__location__ = os.getcwd()

filename = os.path.join(__location__ + "/src/json/acs.json")
filename = os.path.normpath(filename)

#if file does not exist, write it
if os.path.exists(filename):
    append_write = "a"
else:
    append_write = "w"
 
token = ''.join(
    random.choice(string.ascii_lowercase + string.digits) for x in range(6)
)
cookies = requests.cookies.RequestsCookieJar()
cookies.set('wikidot_token7', token, domain='www.scp-wiki.net', path='/')
p = requests.post('http://www.scp-wiki.net/ajax-module-connector.php', data={
    'wikidot_token7': token, 
    'page_id': '858310940', 
    'moduleName': 'backlinks/BacklinksModule'},
    cookies=cookies)

response = json.loads(p.text)

#loading soup

soup = BeautifulSoup(response['body'], 'html.parser')
with open(filename, append_write) as f:
    f.seek(0)
    f.truncate()
    links = soup.find_all("a")
    acsscp = []
    for link in links:
        if "fragment" in link.get("href"):
            continue
        if "edit" in link.get("href"):
            continue
        if "http" in link.get("href"):
            continue
        #print(a.get_text(strip=True))
        acsscp.append(link.get("href"))
        if "scp-" in link.get("href"):
            f.write(str(link.get("href")))
        #json.dump(soup, f, ensure_ascii=False, indent=4)