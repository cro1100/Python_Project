#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import modules needed, OS and CSV
import os
import csv


# In[2]:


# create the path name to access the bank data in a csv file and use it
pollpath = os.path.join( 'Resources', 'election_data.csv')


# In[9]:


# open the csv to begin looping through
with open(pollpath) as polldata:
    poll_reader = csv.reader(polldata, delimiter = ',')
# skip the header row
    header = next(poll_reader)
    
# initiate candidates and votes lists.  These will track who has received a vote and how many votes they received.
    already_listed = False
    candidates = []
    votes = []
    
# read the rows of each voters choice
    for row in poll_reader:
    # test if the data is in the list of candidates; if it is, add one to their votes, already_listed to true & break the loop
    # if not, set already_listed to false, which will be the test for appending

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

#sum of the votes, or total number of voters
voters = sum(votes)

#print out the results
print('Election Results')
print('------------------------')
print(f'Total Votes: {voters}')
            
print()
print(candidates)
print(votes)


    
    


# In[ ]:





# In[ ]:




