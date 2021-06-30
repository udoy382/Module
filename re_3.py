# Corey Schafer / Python Tutorial: re Module

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWNYZ

Ha HaHa

MetaCharacters (Need to be escaped):
. * ^ + - # @ {} () [] | > <

coreyms.com
google.com
facebook.com

0
9

321-555-4321
123.444.1234
111*222*3333
800-222-3333
900-222-3333

Mr. Udoy
Mr Smith
Ms. Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''
sentence = 'Start a sentence and then bring it to an end'

#-------------------
'''
# print(r'\tTab') # if im set [ r ] in first then \t or moroe argiments giving so print same text

# pattern = re.compile(r'abc') # search only abc on the string

# pattern = re.compile(r'.') # [ . ] meens everythin, print all the string

# pattern = re.compile(r'\.') # [ \. ] meens print only all [ . ]

# pattern = re.compile(r'google\.com') # search url

# pattern = re.compile(r'\d') # search only all numbers

# pattern = re.compile(r'\D') # search everything without numbers or digit

# pattern = re.compile(r'\w') # search lowercase digit or uppercase digit or number

# pattern = re.compile(r'\W') # no number no upper or lower case gigit only [ . _ [] () ^ ] as so on

# pattern = re.compile(r'\s') # match only space or new line carecture

# pattern = re.compile(r'\S') # search everything without space or new line careture

# pattern = re.compile(r'\bHa') # search two Ha but there are three Ha cause one Ha is singel or two ha is added
                            # print one single Ha and print one added Ha but not print last adding Ha

# pattern = re.compile(r'\BHa') # this is search word boundary, search last adding Ha

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# print(text_to_search[1:4])
'''

#---------------
'''
# Pattern = re.compile(r'^Start') # srarch start carecture [ ^ ] this sing show first word

# Pattern = re.compile(r'end$') # search end carecture [ $ ] this sing show end word

# Pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # search a phone number on strign show all type of phone number like . - * all

# Pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # metch only [ . ] or [ - ] number 

# Pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') # search 800 or 900 first digit number

# Pattern = re.compile(r'[a-zA-Z]') # search [1-5], [a-z], [A-Z], or [a-zA-Z] 

# Pattern = re.compile(r'[^a-zA-Z]') # [ ^ ] this carecture print everything but cannot print lower or upper case latter a to z or A to Z does not print

# Pattern = re.compile(r'[^b]at') # print all last at item but not print first b items

# Pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # search number in another way

Pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # match name with mr or ms or mrs

# matches = Pattern.finditer(sentence) # this lines for first two line
matches = Pattern.finditer(text_to_search)
for match in matches:
    print(match)
'''

#       matches number on text file [ dada.txt ]
'''
# Pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
Pattern = re.compile(r'\d{5}-\d{6}')
with open('data.txt', 'r') as f:
    content = f.read()
    matches = Pattern.finditer(content)

    for match in matches:
        print(match)
'''

#       match emails
"""
emails = '''
Udoy436@gmail.com
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-312-schafer@my-work.net
'''

# Pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') # metch 2nd email
# Pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') # match 3rd email
# Pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') # match 4th email
# Pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.com') # metch 1st email
# Pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+') # match all emails

matches = Pattern.finditer(emails)
for match in matches:
    print(match)
"""

#       match urls
"""
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

Pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#       this two line print only url name without https or www
# bubbed_urls = Pattern.sub(r'\2\3', urls)
# print(bubbed_urls)

matches = Pattern.finditer(urls)
for match in matches:
    print(match)
    # print(match.group(1)) # we also see every group info
"""

'''
Pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = Pattern.findall(text_to_search)
for match in matches:
    print(match)
'''
#       match function return tuple, match function only show first word not middle or last word
'''
Pattern = re.compile(r'Start')
matches = Pattern.match(sentence)

print(matches)
'''
#       search on the string if search is match return re.match with info without return none
'''
Pattern = re.compile(r'Start')
matches = Pattern.search(sentence)

print(matches)
'''
#       re.IGNORECASE flag
'''
Pattern = re.compile(r'start', re.IGNORECASE)
matches = Pattern.search(sentence)

print(matches)
'''
