import os 
import csv

budgetcsv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

   

with open(budgetcsv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total_months = 0
    net_total = 0


    lines = csvfile.readlines()

data = []

for line in lines[0:]:
        line = line.strip("\n") #erase the newline character from each line
        data.append(line.split(",")) #split the lines using the comma as a delimiter

change = []

for index,element in enumerate(data[1:]): #we start in the second element because we will subtract the first one
        change.append(int(element[1])-int(data[index][1]))

average = sum(change)/len(change)


with open(budgetcsv, 'r') as csvfile:        
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)


    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

print(total_months)
print(net_total)
print(average)
print(max(change))
print(min(change))

        
        

# #     #Create Financial Analysis Printout

    # print(f"Financial Analysis
    # -----------------------
    # Total Months: str(total_months)