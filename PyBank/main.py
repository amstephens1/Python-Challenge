import os 
import csv

budgetcsv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(budgetcsv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total_months = len(list(csvreader))
    #Create Financial Analysis Printout
    print(total_months)

