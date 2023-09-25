# Modules

import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'election_data.csv')

# Read CSV
with open(csvpath, encoding='utf') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# to skip header
    csv_header = next(csvfile)

    print(csv_header)

# count total votes in data
with open(csvpath, "r") as f:
    reader = csv.reader(f,delimiter =",")
    data = list(reader)
    row_count = len(data)
    total_votes = row_count-1

print(f"Total Votes: {total_votes}")

# variables for vote count
charles_vote = 0
diana_vote = 0
raymon_vote = 0

# Calculate vote totals for the candidates
with open(csvpath) as g:
    reader = csv.reader(g,delimiter =",")

    for rows in reader:
        rows

        if rows[2] == "Charles Casper Stockham":
            charles_vote += 1
        elif rows[2] == "Diana DeGette":
            diana_vote += 1
        elif rows[2] == "Raymon Anthony Doane":
            raymon_vote += 1

# To calculate percentage won by each candidate
charles_percent = round(charles_vote / total_votes * 100, 3)
diana_percent = round(diana_vote / total_votes * 100,3)
raymon_percent = round(raymon_vote / total_votes * 100,3)


# Print election results
print(f"Charles Casper Stockeham: {charles_percent}% ({charles_vote})") 
print(f"Diana DeGette: {diana_percent}% ({diana_vote})")
print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_vote})")

print("Winner: Diana DeGette")

# Print election results to text file
f = open("election_results.txt", "w")
print("Election_Results", file=f)
print("________________________________", file=f)
print(f"Total Votes: {total_votes}", file=f)
print("________________________________", file=f)
print(f"Charles Casper Stockeham: {charles_percent}% ({charles_vote})", file=f) 
print(f"Diana DeGette: {diana_percent}% ({diana_vote})", file=f)
print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_vote})", file=f)
print("________________________________", file=f)
print("Winner: Diana DeGette", file=f)
print("________________________________", file=f)
f.close()