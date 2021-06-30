# CodeWithHarry / Json Module

import json

#       json.loads
data = '{"var1":"Udoy", "var2":56}'
# print(data['var1']) # this line show error cause this is not json this is dict

parsed = json.loads(data)
# print(parsed['var1']) # this line print value without error cause it is json
# print(type(parsed))

#       json.dump
data2 = {
    "name":"Saifur Rahman Udoy",
    "age":"17",
    "country":"Bangladesh",
    "cars":['bmw', 'audi', 'ferrari'],
    "fridge":('roti', 'cooke', 'ice-crime'),
    "isbad":False
}

jscomp = json.dumps(data2)
# print(jscomp)

