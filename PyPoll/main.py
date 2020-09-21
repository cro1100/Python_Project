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
# The inner loop comprehension will be the shortened list of the candidates and the number of 
# votes which they have gained.  It's essentially a pivot table.
# The outer loop will be a for loop which runs through the entire list itself to step through 
# each row to pass the data on to the list comprehension.
# The final output will be both a printout of the results and a csv file of the data itself.

# Import modules needed, OS and CSV
import os
import csv
from operator import itemgetter

# create the path name to access the bank data in a csv file and use it
pollpath = os.path.join( 'Resources', 'election_data.csv')

# open the csv to begin looping through
with open(pollpath) as polldata:
    poll_reader = csv.reader(polldata, delimiter = ',')
# skip the header row
    header = next(poll_reader)
    
# initiate candidates and votes lists.  These will track who has received a vote and how many votes they received.
    already_listed = False
# not that originally I wanted to directly create an array for the returned values.  Instead, Wei suggested I use 
# 2 separate lists.
    candidates = []
    votes = []
    
# read the rows of each voters choice
    for row in poll_reader:
    # test if the data is in the list of candidates; if it is, add one to their votes, 'already_listed' to true & break the loop
    # if not, set 'already_listed' to false, which will be the test for appending

        for cndidt in candidates:
            if cndidt == row[2]:
                votes[candidates.index(cndidt)] += 1   #add a vote for the candidate if it matches the list
                already_listed = True                  #set to true to not append the list
                break
            else:
                already_listed = False
        if already_listed == False:
            candidates.append(row[2])
            votes.append(1)

# sum of the votes, or total number of voters
voters = sum(votes)

# zip the two files into a single list then sort correctly
results = list(zip(candidates, votes))
sorted(results,key=lambda x: (x[1]))

# print out the results
print('')
print('Election Results')
print('------------------------')
print(f'Total Votes: {voters}')
print('------------------------')

# I had help with the formatting from stack overflow
for i in range(len(candidates)):
    percentage_votes = "{:.4%}".format(results[i][1] / voters)
    print(f'{results[i][0]}: {percentage_votes} ({results[i][1]})')

# winner
print(f'Winner: {results[0][0]}')

