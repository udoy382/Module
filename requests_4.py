# PyPros / Python Requests *

import requests
from requests.models import Response

#       get requests
'''
payload = {
    "firstname":"udoy",
    "lastname":"rahman"
}
r = requests.get('https://httpbin.org/get', params=payload)

# print(r.url)
# print(r.status_code)
# print(r.content)
# print(r.text)
'''

#       post requests
'''
payload = {
    "firstname":"udoy",
    "lastname":"rahman"
}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

#       upload a file
'''
url = 'https://httpbin.org/post'

#       upload a single file in server
# files = {'file':open('UsCarBrands.csv', 'rb')}

#       uploas a multipul file in server
files = {
    ('copy1', ('UsCarBrands.csv', open('UsCarBrands.csv', 'rb'), 'csv')),
    ('copy2', ('UsCarBrands.csv', open('UsCarBrands.csv', 'rb'), 'csv'))
}

r = requests.post(url, files=files)
# print(r.status_code)
print(r.text)
'''

#       JSON
'''
data = {'firstname':'udoy'}
r = requests.post('https://httpbin.org/post', json=data)
print(r.text)


r = requests.get('https://api.github.com/events')
events = r.json()
# print(events[0])
# print(events[0] ['id'])
'''

#       HTTP Headers
'''
headers = {'content-type':'multipart/form-data'}

r = requests.post('https://httpbin.org/post', headers=headers)
# print(r.request.headers)
# print(r.headers)
print(r.headers['Content-type'])
'''

#       Cookies
'''
url = "https://httpbin.org/cookies"

cookies = {'location':'New York'}

r = requests.get(url, cookies=cookies)
# print(r.text)

r2 = requests.get('https://google.com')
# print(r2.cookies['1P_JAR'])
'''

#       Error Handiling
'''
r = requests.get("https://httpbin.org/status/500") # change status code in url to show which type of error it is
# r.raise_for_status()


r = requests.get("https://httpbin.org/status/200", timeout=0.1)
'''

#       Redirection
'''
# r = requests.get('http://github.com')
# print(r.url)
# print(r.status_code)
# print(r.history)

# r = requests.get('http://github.com', allow_redirects=False)
# print(r.history)


r = requests.head('http://github.com', allow_redirects=True)
print(r.url)
print(r.history)
'''

#       Sessions
'''
#       how to add cookies in server
s = requests.Session()

userName = {'userName':'udoy436'}
location = {'location':'NewYork'}

setcookieUrl = 'https://httpbin.org/cookies/set'
getCookiesUrl = 'https://httpbin.org/cookies'

s.get(setcookieUrl, params=userName)
s.get(setcookieUrl, params=location)

r = s.get(getCookiesUrl)
print(r.text)
'''

#       Event Hooks
'''
def response_info(r, *args, **kwargs):
    print(r.status_code, r.url)
    print(r.text)

def response_headers(r, *args, **kwargs):
    print(r.headers)

hooks = {'response': (response_info, response_headers)}

r = requests.get('https://httpbin.org/get', hooks=hooks)
'''

#       SSL

s = requests.Session()
s.verify = 'path/to/CAs'

r = requests.get('https://github.com',  verify='path/to/CAs') # verify keyword to be False
