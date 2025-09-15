import csv
filename = 'file.csv'

with open(filename, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)