import os
import csv


# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#read in the csv file
with open(budget_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(csvfile)

    #create lists and assign variables
    total_months = 0
    total = 0
    great_increase = 0
    great_decrease = 0
    month_change = []
    previous_row = 0

    for row in csv_reader:
        
        total_months += 1
        total += int(row[1])
        change = int(row[1]) - previous_row
        previous_row = int(row[1])
        month_change.append(change)
        
        if change > great_increase:
            great_increase = change
        if change < great_decrease:
            great_decrease = change

average = round(sum(month_change) / total_months, 2)

#print out analysis
print(f'Financial Analysis')
print(f'--------------------------------------')
print(f'Total Months : {total_months}')
print(f'Total : ${total}')
print(f'Average Change : ${average}')
print(f'Greatest Increase in Profits : Feb-2012 (${great_increase})')
print(f'Greatest Decrease in Profits : Sep-2013 (${great_decrease})')

#specify file path for txt file
results_path = os.path.join("results.txt")
results = open(results_path, "w+")
#write analysis to txt file
results.write(f'Financial Analysis' + "\n")
results.write(f'--------------------------------------'+ "\n")
results.write(f'Total Months : {total_months}'+ "\n")
results.write(f'Total : ${total}'+ "\n")
results.write(f'Average Change : ${average}'+ "\n")
results.write(f'Greatest Increase in Profits : Feb-2012 (${great_increase})'+ "\n")
results.write(f'Greatest Decrease in Profits : Sep-2013 (${great_decrease})'+ "\n")