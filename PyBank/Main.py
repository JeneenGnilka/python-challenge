# Modules

import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# variable to count date

# Read CSV

with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvfile)

    
    # Calculate total profit/loss
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])


# count months in data
with open(csvpath, "r") as f:
    reader = csv.reader(f,delimiter =",")
    data = list(reader)
    row_count = len(data)

print (f"Monthes: {row_count-1}")
print(f"Total: ${total}")
    


    


