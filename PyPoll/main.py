import os

import csv

electioncsv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(electioncsv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    voter_id = []
    county = []
    candidate = []
    candidate_name = []
    votes = []

    k= "Khan"
    c= "Correy"
    l= "Li"
    o= "O'Tooley"

    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    header = next(csvreader)

    for row in csvreader:
        voter_id.append(str(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))

for name in candidate:
    if name not in candidate_name:
        candidate_name.append(name)
        votes.append(1)
    else:
        candidate_name_index = candidate_name.index(name)
        votes[candidate_name_index] += 1
max_vote=0
max_candidates = []
for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes [i]
        candidate_name = candidate_name[i]
        max_candidates = []
        max_candidates.append(candidate_name)



for vote in candidate:
    if vote == k:
        khan_count=khan_count+1
    if vote == c:
        correy_count=correy_count+1
    if vote == l:
        li_count=li_count+1
    if vote == o:
        otooley_count=otooley_count+1


total = int(len(voter_id))
khan = int(khan_count)
correy = int(correy_count)
li = int(li_count)
otooley = int(otooley_count)

khan_percent = (khan_count/total)*100
correy_percent = (correy_count/total)*100
li_percent = (li_count/total)*100
otooley_percent = (otooley_count/total)*100


print("Election Results")
print("-----------------------")
print("Total Votes: "+ str(len(voter_id)))
print("-----------------------")
print("Khan: " + str(round(khan_percent,3)) + "%" + " ("+str(khan_count)+")")
print("Correy: " + str(round(correy_percent,3)) + "%" + " ("+str(correy_count)+")")
print("Li: " + str(round(li_percent,3)) + "%" + " ("+str(li_count)+")")
print("O'Tooley: " + str(round(otooley_percent,3)) + "%" + " ("+str(otooley_count)+")")
print("-----------------------")
print("Winner:" + str(max_candidates))
print("-----------------------")

output_file = os.path.join('PyPoll', 'Analysis', "output.txt") 

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    datafile.writelines("Election Results\n")
    datafile.writelines("--------------------------------\n")
    datafile.writelines("Total Votes: "+ str(len(voter_id)) + "\n")
    datafile.writelines("--------------------------------\n")
    datafile.writelines("Khan: " + str(round(khan_percent,3)) + "%" + " ("+str(khan_count)+")"+ "\n")
    datafile.writelines("Correy: " + str(round(correy_percent,3)) + "%" + " ("+str(correy_count)+")"+ "\n")
    datafile.writelines("Li: " + str(round(li_percent,3)) + "%" + " ("+str(li_count)+")"+ "\n")
    datafile.writelines("O'Tooley: " + str(round(otooley_percent,3)) + "%" + " ("+str(otooley_count)+")"+ "\n")
    datafile.writelines("--------------------------------\n")
    datafile.writelines("Winner:" + str(max_candidates)+ "\n")
    datafile.writelines("--------------------------------\n")
