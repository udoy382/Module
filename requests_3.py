import requests
from requests.api import get

r = requests.get('https://xkcd.com/353/')
# 
# print(r)
# print(dir(r)) # see all methos on this site
# print(help(r)) # see help

# print(r.text) # see htmp text on this site

# print(r.status_code)
# print(r.ok)
# print(r.headers)

#       how to download image with url
'''
r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)

with open('comic.png', 'wb') as f:
    f.write(r.content)

'''

#       how to add dict in last in url
'''
payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params=payload)

# print(r.text)
print(r.url)
'''

'''
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

# print(r.text)
# print(r.json())

r_dict = r.json()
print(r_dict['form'])
'''

#       basic Authentication
'''
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

# print(r.text)
print(r)
'''

# r = requests.get('https://httpbin.org/basic-auth/corey/testing', timeout=3)
r = requests.get('https://httpbin.org/delay/6', timeout=3)

# print(r)