# Python_Project

# PyBank:
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

# I will begin with importing the csv file.  Next I'll run through it and create a list.  
# I'm using the creation of a list rather than accessing the class directly to make it 
# easier to create the previous changes in profit. Through the loop I'll create the summary of information.
# The final output will not only be a printing to the terminal but also a text file with the 
# above information.



# PyPoll:
# The purpose of this code is to count the votes for an election.  Data given is the voter ID, County, Candidate.  
# From this we must report: The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Output looks like:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan

# With this I would like to create list comprehensions rather than just doing for loopsl
# Unfortunately, the for loops became more complicated for my taste and i did no create comprehensions
# The inner loop will be the shortened list of the candidates and the number of 
# votes which they have gained.  It's essentially a pivot table.
# The outer loop will be a for loop which runs through the entire list itself to step through 
# each row to pass the data on to the list comprehension.
# The final output will be both a printout of the results and a csv file of the data itself.
