import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#read in the csv file
with open(election_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvfile)

    total_votes = 0

    for row in csv_reader:
        total_votes += 1





#print out analysis
print(f'Financial Analysis {total_votes}')


results_path = os.path.join("results.txt")
results = open(results_path, "w+")
#print out analysis
results.write(f'Financial Analysis' + "\n")
