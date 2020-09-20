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

# Import modules needed, OS and CSV
import os
import csv

# create the path name to access the bank data in a csv file and use it
bankpath = os.path.join( 'Resources', 'budget_data.csv')
total_profit_loss = 0
profit_change_low = 0
profit_change_high = 0
i = 4

# open the csv and store to a list
with open(bankpath) as bankdata:
    budget_reader = csv.reader(bankdata, delimiter = ',')
    budget_list = list(budget_reader)

# find number of rows in the list for the number of months, subtract 1 to eliminate header   
    total_months = len(budget_list) - 1

# for loop for the sum of all profits/losses
    for row in range(2, total_months):
        total_profit_loss += int(budget_list[row][1])
 
# for loop to find the changes in profits. 
    for row in range(4, total_months):
        i += 1
        profit_change_prev = int(budget_list[row-1][1]) - int(budget_list[row-2][1])
        profit_change_current = int(budget_list[row][1]) - int(budget_list[row-1][1])
     #now test if the profits are greater or lower. Change the variables of the amount and location as needed
        if profit_change_current < profit_change_low:
            profit_change_low = profit_change_current
            low_location = i
        if profit_change_current > profit_change_high:
            profit_change_high = profit_change_current
            high_location = i
                
#create the variabls for the avg loss
avg_profit_loss = int(total_profit_loss / total_months)

#print results to the screen
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${avg_profit_loss}')
print(f'Greatest Increase in Profits: {budget_list[high_location][0]} ${profit_change_high}')
print(f'Greatest Increase in Profits: {budget_list[low_location][0]} ${profit_change_low}')

#create the csv file, starting with concatenating the results
output_results = [total_months, total_profit_loss, avg_profit_loss, budget_list[high_location][0], profit_change_high, budget_list[low_location][0],profit_change_low]
print(output_results)
output_file = os.path.join('PyBank_result.csv')

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total_Months", "Total", "Average_Change","Greatest Increase in Profits month","Greatest Increase in Profits amount",
                    "Greatest Decrease in Profits month", "Greatest Decrease in Profits amount"])  

    writer.writerow(output_results)
    
    
