import os
import csv

#relative file path of the budget data csv file - pybank\Resources\budget_data.csv
budget_data = os.path.join("pybank", "Resources", "budget_data.csv")

#create lists to store data
Date = []
Profit_Losses = []
change = []
total_months = 0
total_profitloss = 0
average_change = 0

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(budget_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 
    previous_profit = 0

   
    #formualas to calculate the data using info from csv file
    for row in csvreader: 

        #add the dates
        Date.append(row[0])
        
    
        #calculate difference between each row and store in empty list
        Profit_Losses.append(int(row[1]))
        if previous_profit == 0: 
            change.append(0)
        else:
            change.append(int(row[1])-previous_profit)
        previous_profit = (int(row[1]))

#calculate the values using info from the lists
number_dates = len(Date)
max_change = max(change)
min_change = min(change)
average = sum(change)/(len(change)-1)
rounded_average = str(round(average, 2))
tot_prof = sum(Profit_Losses)

#print results in terminal
print("Financial Analysis")
print("-------------------------------")

#total number of months in dataset
print("Total Months:", number_dates)

#net total amount of profit/losses over entire period
print(f"Total: ${tot_prof}")

#changes in profit/losses over the entire period, then average of those
print(f"Average Change: ${rounded_average}")

#greatest increase in profits (date and amount) over entire period
print(f"Greatest Increase in Profits: {Date[change.index(max_change)]} (${max_change})")

#greatest decrease in profits (date and amount) over entire period
print(f"Greatest Decrease in Profits: {Date[change.index(min_change)]} (${min_change})")

#export and print the results to .txt file

with open("pybank_solution.txt", "a") as f:

    print("Financial Analysis", file=f)
    print("-------------------------------", file=f)
    print("Total Months:", number_dates, file=f)

    print(f"Total: ${tot_prof}", file=f)

    print(f"Average Change: ${rounded_average}", file=f)

    print(f"Greatest Increase in Profits: {Date[change.index(max_change)]} (${max_change})", file=f)

    print(f"Greatest Decrease in Profits: {Date[change.index(min_change)]} (${min_change})", file=f)
