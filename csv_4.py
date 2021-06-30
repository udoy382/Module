# GeeksforGeeks / from web

#           Reading a CSV file
'''
# importing csv module
import csv

# csv file name
filename = "user.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open (filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

#  printing first 5 rows
print('\nfirst 5 rows are:\n')
for row in rows:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')
'''

#           Writing to a CSV file
'''
# importing the csv module
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [
    ['Udoy', 'COE', '2', 9.0],
    ['Maryam', 'COE', '2', 9.5],
    ['Fariha', 'IT', '1', 8.0],
    ['Mitu', 'SE', '2', 9.0],
    ['Amy', 'MCE', '1', 7.4],
    ['Nadiya', 'EP', '2', 9.1]
]

# name of csv file
filename = "collage_records.csv"

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvweiter = csv.writer(csvfile)

    # writing the fields
    csvweiter.writerow(fields)

    # writing the data rows
    csvweiter.writerows(rows)
'''

#           Writing a dictionary to a CSV file
'''
# importing the csv module
import csv

# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']


# name of csv file
filename = "collage_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    weiter = csv.DictWriter(csvfile, fieldnames = fields)

    # writing headers (field names)
    weiter.writeheader()

    # writing data rows
    weiter.writerows(mydict)
'''
