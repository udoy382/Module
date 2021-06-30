# w3school / from web

import json

# Convert from JSON to Python:
'''
# some JSON:
x = '{"name":"udoy", "age":17, "city":"New York"}'

# parse x:
y = json.loads(x)
# print(y)

# the result is a Python dictionary:
print(y["age"])
'''

# Convert from Python to JSON:
'''
# a Python object (dict):
x = {
    "name":"Saifur Rahman Udoy",
    "age":17,
    "city":"New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
'''
#-----------------------
'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''

# Convert Python objects into JSON strings, and print the values:
'''
print(json.dumps({"name":"udoy", "age":17}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello string"))
print(json.dumps(436))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''

# Convert a Python object containing all the legal data types:
'''
x = {
    "name":"Saifur Rahman Udoy",
    "age":17,
    "married":True,
    "divorced":False,
    "children":("Ann", "Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230", "mpg":27.5},
        {"model":"Ninja H2R", "mpg":25.5}
    ]
}

print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, sort_keys=True))
'''
