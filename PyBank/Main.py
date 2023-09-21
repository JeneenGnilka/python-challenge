# Modules
from collections import Counter
import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# variable to count date

# Read CSV

with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])

    averagechg = (total / 86)

    print(f"Total: $ {total}")

    

length = len(int[1])

count = len(csvfile['date'])

print(averagechg)


print(length)

print(max(row[1]))

    


    


