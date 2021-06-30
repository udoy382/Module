# Amulya's Academy / Calendar Module

import calendar

#       how to print any year's - month's - calendar's
x = calendar.month(2021, 5)
# print(x)

#       how to print calendar in a year
y = calendar.calendar(2021)
# print(y)

z = calendar.weekday(2021, 5, 19)
# print(z)

#       find leap year on this functions
m = calendar.isleap(2021)
# print(m)

#       fine how much leap year in 2000 to 2021 years
n = calendar.leapdays(2000, 2021)
# print(n)

# help(calendar)

o = calendar.monthcalendar(2021, 5)
# print(o)

p = calendar.week()
print(p)