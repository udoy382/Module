# Slomplilearn / Python Regular Expressions (RegEx)

import re

str = "Abcd4 computer 765 Python 687"

str2 = '''
apple
banana
orange
peach
avocado
cherries
'''

str3 = '''
dfax@gmail.com
udoy436@gmail.com
tigacharmo34@yahoo.com
abczyz123@aol
'''
#--------------------
'''
# pattern = r'[a-zA-Z]+'
# pattern = r'[0-9]+'
# pattern = r'[a-zA-Z0-9]+'
# pattern = r'[^ ]+'

match = re.findall(pattern, str)

print(match)
'''
#------------------------
'''
# Pattern = r'.*s'
Pattern = r'\b[aeiou].+\b'

match = re.findall(Pattern, str2)
for i in match:
    print(i)
'''

#----------------

pattern = r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'

match = re.finditer(pattern,str3)
for i in match:
    # print(i.span())
    # print(i.start())
    # print(i.string)
    # print(i.end())
    # print(i.group())
    # print(i.groupdict())
    print(i)