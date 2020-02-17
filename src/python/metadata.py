import os
import requests
import json
import string
import random
from bs4 import BeautifulSoup
import pprint

#open file in working directory
__location__ = os.getcwd()

filename = os.path.join(__location__ + "/src/json/metadata.json")
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
    'page_id': '43035912', 
    'moduleName': 'history/PageRevisionListModule'},
    cookies=cookies)

response = json.loads(p.text)

#loading soup

soup = BeautifulSoup(response['body'], 'html.parser')
firstRevisionID = soup.find('tr', id=lambda x: x and x.startswith('revision-row-'))
firstRevision = firstRevisionID.find(
    'input',
    type="radio"
    ).get("id")

r = requests.post('http://www.scp-wiki.net/ajax-module-connector.php', data={
    'wikidot_token7': token, 
    'revision_id': firstRevision, 
    'moduleName': 'history/PageVersionModule'},
    cookies=cookies)

page_response = json.loads(r.text)
page_soup = BeautifulSoup(page_response['body'], 'html.parser')
table = page_soup.find('table', attrs={'class':'wiki-content-table'})
headers = [header.text for header in table.find_all('th')]
data = [{headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all('td'))}
           for row in table.find_all('tr')]
#data = []
#table = page_soup.find('table', attrs={'class':'wiki-content-table'})
#rows = table.find_all('tr')
#for row in rows:
    #cols = row.find_all('td')
    #cols = [ele.text.strip() for ele in cols]
    #data.append([ele for ele in cols])

metadata_table = ['name','user','type','date']

data = [x for x in data if x]

meta_length = len(metadata_table)
data_length = len(data)
data_dict = {}

#for y in range(data_length):
    #data_temp = {}
    #data_temp[y] = {}
    #for z in range(meta_length):
        #data_temp[y][z] = {metadata_table[z]: data[y][z]}
        #print(data_temp)        
    #data_temp[y] = data_temp_2
    #data_dict.update(data_temp)

with open(filename, append_write) as f:
    f.seek(0)
    f.truncate()
    json.dump(data, f, ensure_ascii=False, indent=4)
