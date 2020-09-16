# This project involves summarizing straightforward profit data of a bank.
# The dataset has 2 columns, date of the summary and profit/Losses.
# The goal is to summarize the time frame in months and to detail the profits and losses 
# during that time, including the total, average changes, and the best and worst months.

# Output looks like:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# I will begin with importing the csv file.  Then I'll run a While loop through all of the data,
# stopping at the first empty row.  Through the loop I'll create the summary of information.
# The final output will not only be a printing to the terminal but also a text file with the 
# above information.

# Import modules needed, OS and CSV
import os
import csv

# create the path name to access the bank data in a csv file and use it
bankpath = os.path.join( 'Resources', 'budget_data.csv')

# open the csv and store to a list
with open(bankpath) as bankdata:
    budget_reader = csv.reader(bankdata, delimiter = ',')
        
# create a while loop to go through all of the bank data
    while 
    
