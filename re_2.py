# edureka! Hindi / Python RegEx in hindi

import re

import urllib.request
from re import findall

nameage = '''Jaince is 22 and Theon is 33
Gabriel is 44 and Joey is 21'''

# print(nameage)


#       find all age
ages = re.findall(r'\d{1,3}',nameage)
# print(ages)


#       find all names 
names = re.findall(r'[A-Z][a-z]*', nameage)
# print(names)


#       make a dict or add name with age
agedic = {}
x = 0
for eachname in names:
    agedic[eachname]=ages[x]
    x+=1

# print(agedic)

#       search any word or caructor using this search method in this string
'''
if re.search('Udoy', 'we need to inform him with Udoy the latest informations'):
    print('There is inform available')
'''

#       search all inform in this giving string 
'''
allinform = re.findall('inform', 'We need to inform him withthe latest information')

for i in allinform:
    print(i)
'''

#       search inform index in this string
'''
str = 'We need to inform him with the latest information'
for i in re.finditer('inform', str):
    loctup = i.span()
    print(loctup)
'''

#       search all at and if s or h or a or r in first join at at printed
'''
str = 'Sat, hat, mat, pat rat'
allstr = re.findall('[shamr]at', str)

for i in allstr:
    print(i)
'''

#       return all without hat or mat
'''
str = 'sat, hat, mat, rat, pat'
somestr = re.findall('[^h-m]at', str)


for i in somestr:
    print(i)
'''

#       chnage rat with food
'''
food = 'hat rat mat pat'
regex = re.compile('[r]at')
food = regex.sub('food', food)
print(food)
'''

#       search full world with [ \\ ] in string
'''
randstr = 'here is \\drogha'
print(randstr)
print(re.search(r'\\drogha', randstr))
'''

#       make a one line in this three line string
"""
randstr = '''keep the blue flag
flying high
chelsea'''

# print(randstr)
regex = re.compile('\n')
randstr=regex.sub(' ', randstr)
print(randstr)
"""

#       search total number, or search any str or any caructor here in this string with using [ \D ] or search how many 5 here with using [ {5} ]
'''
randstr = '123456'
print('Matches:', len(re.findall('\d{5}', randstr)))
'''

#       find 5 to 7 unser number in this string
'''
num = "123 1234 12345 123456 1234567"
print("Matches:", len(re.findall('\d{5,7}', num)))
'''

#       search number
'''
# \w or \d work =  [a-z], [A-Z], [0-9] # \d is good choice for find a phone number cause \d search only number not str or other
# \W or \d work = [^a-zA-Z0-9_] # \d is good choice for find a phone number cause \d search only number not str or other

phn = "412-555-1212"

if re.search('\d{3}-\d{3}-\d{4}', phn):
    print("It is a phone number")
'''

#       search valid name
'''
if re.search('\w{2,20}\s\w{2,20}', 'Udoy Rahman'):
    print("Full name is valid")
'''

#       search email adress on any string
'''
email = 'udoy436@gmail.com ud@.com 436.com yahoo.com sru.com rahul@congitior.com'
print('Email Matches:', len(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', email)))
'''

#       search number in web in this web link 
'''
url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.request.urlopen(url)
html = response.read()
htmlstr=html.decode()
pdata = findall("\(\d{3}\) \d{3}-\d{4}", htmlstr)

for item in pdata:
    print(item)
'''