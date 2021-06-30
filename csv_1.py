# Corey Schafer / Python Tutorial: CSV MOdule

import csv

# first we open csv file then this csv file read, then open new csv file and fush all text from csv file to new csv file
'''
with open('user.csv', 'r') as csv_file:
    csv_rider = csv.reader(csv_file)

    # print(csv_rider)
    # next(csv_rider)

    with open('new_user.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

    # for line in csv_rider:
    #     # print(line)
    #     print(line[2]) # print all emils index 2

        for line in csv_rider:
            csv_writer.writerow(line)
'''

'''
with open('user.csv', 'r') as csv_file:
    csv_rider = csv.DictReader(csv_file)

    for line in csv_rider:
        # print(line)
        print(line['email']) # access any key
'''

'''
with open('user.csv', 'r') as csv_file:
    csv_rider = csv.DictReader(csv_file)

    with open('new_user.csv', 'w') as new_file:
        # fieldnames = ['first_name', 'last_name', 'email'] #>>> 1
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_rider:
            del line['email'] #>>> 1, deleted email on csv file
            csv_writer.writerow(line)
'''