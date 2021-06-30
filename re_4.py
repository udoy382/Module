# edureka! / Python RegEx

import re

Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joye is 21
'''

#       match name and age with dict form
'''
ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}

x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1

print(ageDict)
'''

#       find anython in string, one method is search or antoher method is findall
'''
# if re.search("inform", "We need to inform him witlh the latest information"):
#     print("There is inform")


allinform = re.findall("inform", "We need to inform him with the latest information")
for item in allinform:
    print(item)
'''

#       search all inform index number in str, i.span() return tuple value
'''
str = 'We need to inform him with the latest information'
for i in re.finditer('inform', str):
    loctup = i.span()
    print(loctup)
'''

#       search all world with findall method
'''
str = 'Sat, hat, mat, pat'
allstr = re.findall(r'[shmp]at', str)

for i in allstr:
    print(i)
'''

#       find range of caructor on the string
'''
str = 'sat, hat, mat, pat'
allstr = re.findall(r'[^h-m]at', str)

for i in allstr:
    print(i)
'''

#       repalce rat with food, replace any item with compile or sub methods
'''
food = "hat rat mat pat"

regex = re.compile('[r]at')
food = regex.sub('food', food)
print(food)
'''

#       solv \\ problem
'''
randstr = "here is \\drogba"
# print(randstr)
print(re.search(r'\\drogba', randstr))
'''

#       replace space, 3 line to 1 line, sub meens repalce 
"""
randstr = '''
Keep the blue flag
flying high
chelsea
'''

print(randstr)

regex = re.compile('\n')
randomstr = regex.sub(' ', randstr)
print(randomstr)
"""

# \b : backspace
# \f : formfeed
# \r : carriage return
# \t : tab
# \v : vartical tab

#       match number 
'''
randstr = '12345'
# print('Matches:', len(re.findall(r'\d{5}', randstr)))

num = '123 1234 12345 123456 1234567'
print('Matches:', len(re.findall(r'\d{5,7}', num)))
'''

# \w : [a-zA-Z0-9]
# \W : [^a-zA-Z0-9]

#       verifyed or match number
'''
phn = "412-555-1212"

if re.search('\w{3}-\w{3}-\w{4}', phn):
    print('it is a phone number')
'''

# \s [\f\n\r\t\v]
# \S [^\f\n\r\t\v]

#       verifyed the name
'''
# if re.search('\w{2,20}\s\w{2,20}', 'Saifur Rahman Udoy'):
#     print("full name is valid")
'''

#       match email address
'''
# email = "sk@aol.com md@.com @seo.com dc@.com sk@aol.com"
# print('EmailMatches:', len(re.findall(r'[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', email)))
'''

#       web scraping

import urllib.request
from re import findall

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.request.urlopen(url)

html = response.read()
htmlstr = html.decode()
pdata = findall('\(\d{3}\) \d{3}-\d{4}', htmlstr)

for item in pdata:
    print(item)