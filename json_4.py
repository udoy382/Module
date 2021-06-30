# edureka! / Python JSON

import json

people_string = '''
{
    "people": [
        {
            "emp_name":"Saifur Rahman Udoy",
            "emp_no":"12334",
            "emp_email":["udoy436@gmail.com"],
            "has_license":"false"
        },
        {
            "emp_name":"Harry",
            "emp_no":"3445",
            "emp_email":"null",
            "has_license":"true"
        }
    ]
}
'''
#--------------------------
'''
data = json.loads(people_string)
print(data)
# print(type(data))

for person in data['people']:
    print(person['emp_name'], person['emp_email'])
'''
#-------------------------
'''
data = json.loads(people_string)
for person in data['people']:
    del person['emp_no']

new_string = json.dumps(data)
print(new_string)
# print(type(new_string))
'''
#----------------------------
'''
with open('states.json') as f:
    data = json.load(f)

for nobel_price in data['states']:
    print(nobel_price['name'],nobel_price['area_codes'])
'''
#----------------------------
'''
with open('states.json') as f:
    data = json.load(f)

for nobel_price in data['states']:
    del nobel_price['area_codes']

with open('new.json', 'w') as f:
    json.dump(data, f, indent=2)
'''