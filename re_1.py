# Code With Harry / Regular Expressions

import re

mystr = '''Hello world, I am a Saifur +8801782-668254 .Rahman Udoy, i aiiii want to learn cybersecurity.
and i am from bangladesh , i am a python programmer. 01782-299436, 1.1.1, 2.2.2, 333, 45, 436
haha hehe huhu 2929, 5454 helo bangladesh India 66-66 hola'''

# all functions = findall, search, split, sub, finditer

# search any carecture in string
'''
# print(r"\n")
patt = re.compile(r'learn')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[50:55])
'''

# search [ . ] or any rarecture in string [ . ] meens all
'''
patt = re.compile(r'.Rahman')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

#  search which caructor first to start in this string [ ^ ] this meen which first carecture in this string
'''
patt = re.compile(r'^Hello')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

#  search which caructor end in this string [ $ ] this meen which end carecture in this string
'''
patt = re.compile(r'hola$')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# [ ai* ] meens a or all i and [ a*i* ] meens all [ a ] and all [ i ]
'''
patt = re.compile(r'ai*')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# see only ai 
'''
patt = re.compile(r'ai+')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# see exject ai in this string
'''
patt = re.compile(r'ai{2}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''
# see exject ai with makeing group, if im search 2 ai so im add 2 in [ {} ] this second bracket
'''
patt = re.compile(r'(ai){1}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# show ai or show t [ | ] this meens [ or ]
'''
patt = re.compile(r'ai{1}|t')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

#       Spcial Sequences

# if Hello first word in this string os show without not  [ \A ] meens which first word in this string
'''
patt = re.compile(r'\AHello')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# return all start word like cyber
'''
patt = re.compile(r'\bcyber')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# return all ending word like security
'''
patt = re.compile(r'security\b')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# search number or anything with desh [ - ] in string
'''
patt = re.compile(r'\d{5}-\d{6}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
'''

# Exercise code...


patt = re.compile(r'\d{7}-\d{6}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)