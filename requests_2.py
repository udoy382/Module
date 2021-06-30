import requests

'''
payload = {'key1':'value1'} # make a variable in  dict 
res = requests.get("https://httpbin.org/get", params=payload) # add payload values with url using params
# print(res.text)
print(res.url)
'''

'''
payload = {'key1':'value1'}
res = requests.post("https://httpbin.org/post", data=payload)

print(res.text)
'''

'''
res = requests.get('https://httpbin.org/get')

# print(res.status_code)
# print(res.cookies)
# print(res.headers)
# print(res.json())
'''

#       how to add cookies in server
'''
cookies = dict(key1='value1')

res = requests.get("https://httpbin.org/cookies", cookies=cookies)
print(res.text)
'''

#       headers
# res = requests.get("https://httpbin.org/headers")
# print(res.headers)

