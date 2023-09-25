# Modules

import os
import csv

# Import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
date = []
profit_loss = []
monthly_change = []
# variables
total_change = 0
prv_month_chg = 0
max_num = 0
# Read CSV
with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    csv_header = next(csvfile)
    print(csv_header)

    # Calculate column of net change of current month compared to prior month
    for row in csv.reader(csvfile):
    

        # Add Date
        date.append(row[0])

        # Add Profit/Loss
        profit_loss.append(int(row[1]))

    # calculate change in Profit/Loss from prior month
    for x, y in zip(profit_loss[0::], profit_loss[1::]):
        monthly_change.append(y-x)


# Total profit
total_P_L = sum(profit_loss)

# Total Months
total_months = (len(date))

# Average Change
import statistics
avg_chg = round(statistics.mean(monthly_change),2)
    

# Print total months
print (f"Months: {total_months}")
# Print total of Profit/Loss
print(f"Total: ${total_P_L}")
# Print Average Change 
print(f"Average Change: {avg_chg}")
# Greatest increase in Profits
print(f"Greatest Increase in Profits: {(date[monthly_change.index(max(monthly_change))+1])} ${(max(monthly_change))}")
# Greatest decrease in profits
print(f"Greatest Derease in Profits: {(date[monthly_change.index(min(monthly_change))+1])} ${(min(monthly_change))}")

# Print Financial Analysis to text file
f = open("Financial_Analysis.txt", "w")
print("Financial Analysis", file=f)
print("________________________________", file=f)
print (f"Months: {total_months}", file=f)
print(f"Total: ${total_P_L}", file=f)
print(f"Average Change: ${avg_chg}", file=f)
print(f"Greatest Increase in Profits: {(date[monthly_change.index(max(monthly_change))+1])} (${(max(monthly_change))})", file=f)
print(f"Greatest Decrease in Profits: {(date[monthly_change.index(min(monthly_change))+1])} (${(min(monthly_change))})", file=f)
f.close()