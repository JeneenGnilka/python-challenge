# Modules

import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
date = []
profit_loss = []
monthly_change = []

prv_month_chg = 0

# Read CSV
with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    csv_header = next(csvfile)

    for row in csv.reader(csvfile):
    

        # Add Date
        date.append(row[0])

        # Add Profit/Loss
        profit_loss.append([1])

        # Calculate change from previous month and add monthly_change
        prv_month_chg = (int(row[1]) - ((row-1)[1]))
        monthly_change.append(int(prv_month_chg))

   # print(date, profit_loss)

# Read CSV
with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first 
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


with open(csvpath, "r") as f:
    reader = csv.reader(f,delimiter =",") 
  
  
  #  Change_Prev_Mon = []
   
   # for i in csv.reader(csvfile):
    #    Change_Prev_Mon.append([0,] + [int[i-1]])

print (f"Monthes: {row_count-1}")
print(f"Total: ${total}")
    


    


