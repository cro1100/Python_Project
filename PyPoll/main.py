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
# The first will simply be a summary of the data with each candidate listed with a sum, 
# hence a list comprehension which loops around all the data. I will then have a smaller list which 

# 
# Import modules needed, OS and CSV
import os
import csv

# create the path name to access the bank data in a csv file and use it
pollpath = os.path.join( 'Resources', 'election_data.csv')


# open the csv and store to a list
with open(pollpath) as polldata:
    poll_reader = csv.reader(polldata, delimiter = ',')
    poll_list = list(oll_reader)