# Code With Harry / Requests module for HTTPS requests

import requests

r = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo")
# print(r.text)

# print(r.status_code) # search on google "http status code"

#       how to work post requests
# url = "www.google.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
# print(r2)