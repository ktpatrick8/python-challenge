import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#read in the csv file
with open(election_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvfile)

    total_votes = 0
    candidates = []
    vote_list = []

    for row in csv_reader:
        total_votes += 1

        name = str(row[2])
        # vote_list.append(name)
        if name not in candidates:
            candidates.append(name)

        if name == candidates[0]:
            vote_list[0] = vote_list[0] + 1


    # def result_calc(vote_list):
    #     vote_count = vote_list.count(value)
    #     vote_percentage = vote_count / total_v

    # khan_votes = vote_list.count("Khan")
    # correy_votes = vote_list.count("Correy")
    # li_votes = vote_list.count("Li")
    # otooley_votes = vote_list.count("O'Tooley")

    # khan_percent = (khan_votes / total_votes) * 100
    # correy_percent = (correy_votes / total_votes) * 100
    # li_percent = (li_votes / total_votes) * 100
    # otooley_percent = (otooley_votes / total_votes) * 100

print(candidates)
print(vote_list)
# print(khan_percent)




# #print out analysis
# print(f'Financial Analysis {total_votes}')


# results_path = os.path.join("results.txt")
# results = open(results_path, "w+")
# #print out analysis
# results.write(f'Financial Analysis' + "\n")
