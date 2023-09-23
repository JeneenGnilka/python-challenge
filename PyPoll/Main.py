# Modules

import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'election_data.csv')

    # Read CSV
with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    print(csvreader)
    print(csv_header)

# count total votes in data
with open(csvpath, "r") as f:
    reader = csv.reader(f,delimiter =",")
    data = list(reader)
    row_count = len(data)

print(f"Total Votes: {row_count-1}")

# variables for vote count
charles_vote = 0
diana_vote = 0
raymon_vote = 0

# Calculate vote totals
with open(csvpath, "r") as g:
    reader = csv.reader(g,delimiter =",")
    votes = list(reader)
    for votes in reader:
        if votes == "Charles Casper Stockham":
            charles_vote += 1
        elif votes == "Diana DeGette":
            diana_vote += 1
        elif votes == "Raymon Anthony Doane":
            raymon_vote += 1

print(charles_vote, " ", diana_vote, " ", raymon_vote)

