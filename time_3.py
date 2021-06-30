# Geeky Shows / Formatting Date and Time in python

'''
Format Code         Meaning                                         Example
--------------------------------------------------------------------------------------------
%a              weekday in short name                           Sun, Mon.....Sat
%A              weekday in full name                            Sunday, Monday....Saturday
%d              Day of month with 0 padded                      01, 02....30,31
%b              Month in short name                             Jan, Feb....Dec
%B              Moonth with full name                           January....December
%m              Month in number with 0 padded                   01, 02....12
%y              Year in short with 0 padded, with century       00, 01, 02....99
%Y              Year in full with century                       0001, 0002.....9999
'''
from datetime import datetime


dt = datetime.today()
print(dt)

newd1 = dt.strftime("%B / %d / %Y")
print(newd1)