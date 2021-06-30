# edureka! How to read CSV file in Python

import csv

#   read a csv file
'''
with open('user.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
'''

#   write a csv file
'''
with open('user.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_csv_file.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)

        for line in csv_reader:
            csv_writer.writerow(line)
'''

#   reade csv file as Dictonary
'''
with open('user.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
'''

#   write csv file as Dictonary
'''
mydict = [{'Passenger':'1', 'Id':'0', 'Survived':'1'},
        {'Passenger':'2', 'Id':'1', 'Survived':'1'},
        {'Passenger':'3', 'Id':'2', 'Survived':'2'}]

fields = ['Passenger', 'Id', 'Survived']

filename = 'new_titanic.csv'

with open(filename, 'w') as new_csv_file:
    writer = csv.DictWriter(new_csv_file, fieldnames=fields, delimiter='-')

    writer.writeheader()
    writer.writerows(mydict)
'''