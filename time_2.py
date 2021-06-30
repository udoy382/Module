# edureka! / Date and Time in python

#------------------------------------
#   Time
#------------------------------------

'''
import time

time1 = time.time()
# print(time1)

#       print current date and time on using this method
ctime = time.ctime(1621313342.4255385)
# print(ctime)


# help(time.time())


x = time.localtime()
print(x)


a = time.localtime()
b = time.mktime(a)
# print(b)

c = time.asctime()
# print(c)

# help(time.strftime)

#       print month / date / year on this method
z = time.strftime("%m/%d/%y")
# print(z)

#       change localtime value on using this method
k = "08 August 2020"
j = time.strptime(k, "%d %B %Y")
# print(j)
'''

#------------------------------------
#   Datetime
#------------------------------------

import datetime

d = datetime.datetime(2021,5,7,4,30,54,678) # year, month, date, time, minute, second, microsecond
# print(d)

#       two method value are same
x = datetime.datetime.today()
y = datetime.datetime.now()
# print(x)
# print(y)

#       we exccess the value on this datetime.today() and datetime.now()
# print(y.year)
# print(x.month)

#       we print date with giving value
m = datetime.date(2021,5,7)
# print(m)

b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=30)
b3 = b1 - b2
print(b3)
print(type(b3))