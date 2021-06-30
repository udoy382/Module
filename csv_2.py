# Corey Schafer /

import csv

'''
html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # print(csv_data) # make csv genenrator
    # print(list(csv_data))


    #       We don't want headers or first line of bad data
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        # print(line)

        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")


#       run code, all names
# for name in names:
#     print(name)

#-------------------

html_output += f'<p>There are currently {len(names)} public contributors, Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n<ul>'

print(html_output)
'''

'''
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    for item in csv_data:
        print(item)
'''