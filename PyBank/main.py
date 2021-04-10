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
        line = line.strip("\n") 
        data.append(line.split(",")) 

change = []

for index,element in enumerate(data[1:]):
        change.append(int(element[1])-int(data[index][1]))
        
average = sum(change)/len(change)


with open(budgetcsv, 'r') as csvfile:        
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    date = []

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        date.append(str(row[0]))

#     #Create Financial Analysis Printout

print("Financial Analysis")
print("--------------------------------")

print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average  Change: $" + str(round(average,2)))
print("Greatest Increase in Profits: $" + str(max(change)))
print("Greatest Decrease in Profits: $" + str(min(change))) 

output_file = os.path.join('PyBank', 'Analysis', "output.txt") 

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    datafile.writelines("Financial Analysis\n")
    datafile.writelines("--------------------------------\n")
    datafile.writelines("Total Months: " + str(total_months) + "\n")
    datafile.writelines("Total: $" + str(net_total)+ "\n")
    datafile.writelines("Average  Change: $" + str(round(average,2))+ "\n")
    datafile.writelines("Greatest Increase in Profits: $" + str(max(change))+ "\n")
    datafile.writelines("Greatest Decrease in Profits: $" + str(min(change))+ "\n") 