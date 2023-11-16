import os
import csv

#relative file path of the election data csv file - pypoll\Resources\election_data.csv
election_data = os.path.join("pypoll", "Resources", "election_data.csv")

#create lists to store data
ballot_id = []
Candidate = []
unique = []
charles_votes = []
diana_votes = []
raymon_votes = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_data, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #formuals to calculate the data using info from csv file
    for row in csvreader: 
       
        #add ballot id's
        ballot_id.append(row[0])

        #add candidate names
        Candidate.append(row[2])

        #group the candidates votes to invdividual lists
        if (row[2]) == "Charles Casper Stockham":
            charles_votes.append(row[0])
        
        if (row[2]) == "Diana DeGette":
            diana_votes.append(row[0])

        if (row[2]) == "Raymon Anthony Doane":
            raymon_votes.append(row[0])


#Finds each unique candidate from the election data.
for x in Candidate:
    if x not in unique:
        unique.append(x)
        len(ballot_id)

#calculate total votes
total_votes = len(ballot_id)
all_candidates = unique

#calculate the total votes and percentage for Charles
total_charles = len(charles_votes)
charles_percent = total_charles/total_votes
format_cpercent = "{:.3%}".format(charles_percent)

#calculate the total votes and percentage for Diana
total_diana = len(diana_votes)
diana_percent = total_diana/total_votes
format_dpercent = "{:.3%}".format(diana_percent)

#calculate the total votes and percentage for Raymon
total_raymon = len(raymon_votes)
raymon_percent = total_raymon/total_votes
format_rpercent = "{:.3%}".format(raymon_percent)

#print results in terminal
print("Election Results")
print("------------------------")

#total number of votes cast
print("Total Votes:", total_votes)
print("------------------------")

#print(all_candidates) - this is used to see confirm each unique candidate from the list, commented out for official results.

#The percentages and total number of votes each candidate won. Percentages were converted to 3 decimal places.
print(f"Charles Casper Stockham: {format_cpercent} ({total_charles})")
print(f"Diana DeGette: {format_dpercent} ({total_diana})")
print(f"Raymon Anthony Doane: {format_rpercent} ({total_raymon})")
print("-------------------------")

#calculates the winner of the election and prints their name
results = {total_charles:"Winner: Charles Casper Stockham",total_diana:"Winner: Diana DeGette",total_raymon:"Winner: Raymon Anthony"}
print(results.get(max(results)))
print("-------------------------")

#export and print the results to .txt file
with open("pypol_results.txt", "a") as f:

    print("Election Results", file=f)
    print("------------------------", file=f)
    print("Total Votes:", total_votes, file=f)
    print("------------------------", file=f)
    print(f"Charles Casper Stockham: {format_cpercent} ({total_charles})", file=f)
    print(f"Diana DeGette: {format_dpercent} ({total_diana})", file=f)
    print(f"Raymon Anthony Doane: {format_rpercent} ({total_raymon})", file=f)
    print("-------------------------", file=f)
    results = {total_charles:"Winner: Charles Casper Stockham",total_diana:"Winner: Diana DeGette",total_raymon:"Winner: Raymon Anthony"}
    print(results.get(max(results)), file=f)
    print("-------------------------", file=f)