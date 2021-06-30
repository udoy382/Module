# from web

import random

mu = 100
sigma = 50
# print(random.gauss(mu, sigma))

#--------------------
# the generator creates a random number 
# based on the seed value, so if the seed value is 10,
# you will always get 0.5714025946899135 as the first random number.

random.seed(10)
# print(random.random())
# print(random.random())

#---------------------
# The getstate() method returns an object
#  with the current state of the random number generator.

# Use this method to capture the state, and use the setstate() method,
#  with the captured state, to restore the state

x = random.getstate()
print(x)

#------------------------
# Return a list with 14 items.
# The list should contain a randomly selection of the values from a specified list,
# and there should be 10 times higher possibility to select "apple" than the other two:
mylist = ["apple", "banana", "cherry"]

# print(random.choices(mylist, weights=[10, 1, 1], k=14))
# print(random.choices(mylist, k = 10))