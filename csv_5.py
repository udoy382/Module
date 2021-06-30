# from web

import csv

# Example 1: Write to a CSV file
'''
with open('app.csv', 'w', newline='') as file:
    weiter = csv.writer(file, delimiter='\t')
    weiter.writerow(["SN", "Movie", "Protagonist"])
    weiter.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    weiter.writerow([2, "Harry Potter", "Harry Potter"])
'''

# Example 2: Writing to a CSV File with Tab Delimiter
'''
with open('app.csv', 'w') as file:
    weiter = csv.writer(file, delimiter='\t')
    weiter.writerow(["SN", "Movie", "Protagonist"])
    weiter.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    weiter.writerow([2, "Harry Potter", "Harry Potter"])
'''
