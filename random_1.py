# Code With Harry / random module

import random


random_number = random.randint(0, 5)
# print(random_number) # return int value


rand = random.random() * 100
# print(rand)


lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
print(choice)