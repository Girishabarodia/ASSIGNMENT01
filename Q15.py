import csv

# Path to your CSV file
csv_file = 'data.csv'

# Read data from CSV file and print it
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(', '.join(row))
