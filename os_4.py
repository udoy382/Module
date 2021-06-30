# from web

import os

cwd = os.getcwd()
# print("current working directory: ", cwd)

#----------------

# def current_path():
#     print("Current working directory before")
#     print(os.getcwd())


# current_path()

# os.chdir('../')

# current_path()

#--------------------

# try:

#     filename = 'GFG.txt'
#     with open(filename, 'rU') as f:
#         text = f.read()

# except IOError:
#     print('Problem reading: ' + filename)

#--------------------------

fd = 'demo.txt'

file = open(fd,'w')
file.write("Saifur Rahman Udoy")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

file = os.popen(fd, 'w')
file.write("Hello")