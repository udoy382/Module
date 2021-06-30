# Corey Schafer / Working with JSON Data using the json Module

import json

people_string = '''
{
    "people":[
        {
            "name":"Udoy",
            "age":"17",
            "phone":"01782299436",
            "emails":["udoy436@gmail.com", "srudoy436@gmail.com"],
            "has_license": false
        },
        {
            "name":"Harry",
            "age":"24",
            "phone":"99017822994",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# print(people_string)

#       we convarted the json to python
# data = json.loads(people_string)
# print(data)
# print(type(data['people']))

#--------------------------------------
#       excess the json data
'''
data = json.loads(people_string)
for person in data['people']:
    # print(person['name'])

    del person['phone']

# new_string = json.dumps(data)
# new_string = json.dumps(data, indent=2)
new_string = json.dumps(data, sort_keys=True) # sort all data
print(new_string)
'''

#----------------------------------------

# [ load ] method used for file and [ loads ] method used for string
'''
with open('states.json', 'r') as f:
    data = json.load(f)

for state in data["states"]:
    # print(state['name'], state['abbrevitiion'])

    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
'''

# work real web json
# website: {JSON} Placeholder , for json url
'''
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/users") as response:
    source = response.read()

data = json.loads(source)
# print(data)
# print(json.dumps(data, indent=2))
'''