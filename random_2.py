# Swati Chawla / random module functions

import random

#       random.randrange shows 0 to 4 random numbers
x = random.randrange(5)
# print(x)


#       this print statment shows 30 to 39 random numbers
y = random.randrange(30, 40)
# print(y)


z = random.uniform(31, 35)
# print(z)


#       random.shuffle changed order value in lst
#       The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
lst = ["C++", "c", "Java", "Python", "JavaScript", "C#"]
random.shuffle(lst)
# print(lst)