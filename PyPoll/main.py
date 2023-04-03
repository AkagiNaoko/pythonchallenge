import csv
import os

candidates={}
totalNumber=0

# print function
def printWrite(sentence):
    print(sentence)
    out_put_path=os.path.join('analysis','analysis.txt')
    file = open(out_put_path, "a")
    file.write(sentence)

# path of resorces
input_path = os.path.join('Resources','election_data.csv')

# open file and overwrite data in dictionary
with open(input_path,'r') as electioncsv_file:
    bank_reader= csv.reader(electioncsv_file)
    bank_reader= next(electioncsv_file)

    for row in electioncsv_file:
        splitData = row.split(',')
        candidate = splitData[2]
        totalNumber = totalNumber +1
        if candidate not in candidates:
            candidates[candidate]=1
        else:
            candidates[candidate]=candidates[candidate]+1
printWrite('Election Results\n-------------------------\n')
printWrite(f'Total Votes: {totalNumber}\n-------------------------\n')

winerNumber=0
votePercent=0
# print and 
# caculate and find the winer
for candidate in candidates:
    votePercent = "%.3f%%" %(float(candidates[candidate])/totalNumber*100)

    printWrite(f'{candidate} : {votePercent} ({candidates[candidate]})\n')
    # find the winner
    if candidates[candidate] > winerNumber:
        winner = candidate
        winerNumber= candidates[candidate]

printWrite(f'-------------------------\n Winner: {winner}\n-------------------------\n')
