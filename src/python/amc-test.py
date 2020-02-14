import requests
import json
import string
import random
 
token = ''.join(
    random.choice(string.ascii_lowercase + string.digits) for x in range(6)
)
cookies = requests.cookies.RequestsCookieJar()
cookies.set('wikidot_token7', token, domain='www.scp-wiki.net', path='/')
p = requests.post('http://www.scp-wiki.net/ajax-module-connector.php', data={
    'wikidot_token7': token, 
    'categoryId': '1900210', 
    'moduleName': 'forum/ForumRecentPostsListModule', 
    'page':'1', 
    'limit':'5'}, 
    cookies=cookies)
response = json.loads(p.text)
body = response['pager-no']
print(body)
