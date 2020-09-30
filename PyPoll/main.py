import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#read in the csv file
with open(election_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')

    #skip header row
    csv_header = next(csvfile)

    #create lists and assign variables
    total_votes = 0
    candidates = []
    vote_counter = []

    #loop through rows in csv file
    for row in csv_reader:

        #total votes counter
        total_votes += 1

        #stores candidate names and vote counts into two lists
        name = str(row[2])
        if name in candidates:
            #looks up index location of name in candidate list. Once you have that index number 
            #you can use that to look up the corresponding value in the vote_counter list
            candidate_index = candidates.index(name)
            vote_counter[candidate_index] = vote_counter[candidate_index] + 1
        else:
            #if name is not already in the list it adds it to candidates and adds 1 vote to vote_counter
            candidates.append(name)
            vote_counter.append(1)

#create more lists and assign variables 
percentage = []
most_votes = vote_counter[0]
winner = 0

for x in range(len(candidates)):
    #loops through and calculates vote % and stores in a new list called percentages
    vote_percentage = round(vote_counter[x] / total_votes * 100, 2)
    percentage.append(vote_percentage)
    
    #loop goes through vote_counter list and determines index location that has the most votes 
    if vote_counter[x] > most_votes:
        most_votes = vote_counter[x]
        winner = x

#returns the name of the winner in the candidates list. Use the index location determined in the if statement above^
election_winner = candidates[winner]

#prints results
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {percentage[x]}% ({vote_counter[x]})")
print("------------------------")    
print(f"Winner: {election_winner}")
print("------------------------")

#specifies the file path for output txt file
results_path = os.path.join("poll.txt")
poll = open(results_path, "w+")

#write output to txt file
poll.write(f"Election Results" + "\n")
poll.write(f"------------------------" + "\n")
poll.write(f"Total Votes: {total_votes}" + "\n")
poll.write(f"------------------------" + "\n")
for x in range(len(candidates)):
    poll.write(f"{candidates[x]}: {percentage[x]}% ({vote_counter[x]})" + "\n")
poll.write(f"------------------------" + "\n")    
poll.write(f"Winner: {election_winner}" + "\n")
poll.write(f"------------------------" + "\n")