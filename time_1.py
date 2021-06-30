# code With Harry / Time module in python

import time

initial = time.time()
# print(initial)

k = 0
while(k<45):
    print("This is udoy bhai")
    time.sleep(2)
    k+=1
print("While loop run in: ", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(54):
    print("This is udoy bhai")
print("For loop run in: ", time.time()-initial2, "Seconds")


#       print local time using this time function
'''
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
'''