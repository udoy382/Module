# Corey Schafer / Python Tutorial: OS Module

import os
from datetime import datetime

# print(dir(os)) # show all method to access in module

# print(os.getcwd()) # get current working directry / current path

# os.chdir('C://') # change dir on this comment

# print(os.getcwd())

# print(os.listdir()) # see all item on this directry or im also add path to see all item 


# os.mkdir('haha') # make one directry on this comment 
# os.makedirs('OS-Demo-2/Sub-dir-1') # make directry into directry on this comment


# os.rmdir('haha') # this method use for remove only directry 
# os.removedirs('OS-Demo-2') # or this method use for remove multipul dirctry


# os.rename('udoy.txt', 'demo.txt') # rename any file or folder on this method

# print(os.stat('demo.txt').st_mtime) # this method show all detials in this directry

#       change to human readable formet time
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))


#       can't understand this code, but it is a importent
# --------------------------------------------------------------
# for dirpath, dirnames, filenames in os.walk('C://'):
#     print('Current Path', dirpath)
#     print('Directoris', dirnames)
#     print('Files', filenames)
# --------------------------------------------------------------

#       this method show what is base name or dirname in this path
# print(os.path.basename('/temp/text.txt'))
# print(os.path.dirname('/temp/text.txt'))
# print(os.path.split('/tmep/text.txt')) # split this path
# print(os.path.exists('/temp/text.txt')) # show this file exists or not in directry
# print(os.path.splitext('/temp/test.txt')) # split text 
# print(os.path)
# print(dir(os.path))
