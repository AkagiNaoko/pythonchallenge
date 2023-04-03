import csv
import os

Dates=[]
ProfitLosses=[]
Changes={}
Start=0
count=1

# path of resorces
input_path = os.path.join('Resources','budget_data.csv')

# open file
with open(input_path,'r') as bankcsv_file:
    bank_reader= csv.reader(bankcsv_file)
    bank_reader= next(bankcsv_file)

 # read the file and store in analysis list and dictionary
    for row in bankcsv_file :
        splitData=row.split(',')
        date=splitData[0]
        ProfitLoss=int(splitData[1])

        # date and profit
        Dates.append(date)
        ProfitLosses.append(ProfitLoss)

        #the changes in Profit-
        if count==1 :
            Start=ProfitLoss
        else:
            Change= ProfitLoss-Start
            Start= ProfitLoss
            Changes[date]=Change 
        count = count +1

print(Changes)

# calculate The total number of months included in the dataset
totalMonthNumber = len(Dates)

# calculate The net total amount of "Profit/Losses" over the entire period
totalAmount = sum(ProfitLosses)

# calculate the change with dictionary Changes
GreatIncrease = 0
GreatDecrease = 0
n=0
SumChange=0
 # The changes in "Profit/Losses" over the entire period, and then the average of those changes
for date in Changes:
    n=n+1
    SumChange = SumChange +int(Changes[date])
    print(Changes[date])

    if int(Changes[date]) > GreatIncrease:
        GreatIncrease = int(Changes[date])
        GreatIncreaseDate = date
    elif int(Changes[date]) < GreatDecrease:
        GreatDecrease = int(Changes[date])
        GreatDecreseDate = date

   # The greatest increase in profits (date and amount) over the entire period
   # The greatest decrease in profits (date and amount) over the entire period
Average=round((SumChange/n),2)

# print function
def printWrite(sentence):
    print(sentence)
    out_put_path=os.path.join('analysis','analysis.txt')
    file = open(out_put_path, "a")
    file.write(sentence)
   

printWrite("Financial Analysis\n")
printWrite("----------------------------\n")
printWrite(f'Total Months: {totalMonthNumber}\n')
printWrite(f'Total: ${totalAmount}\n')
printWrite(f'Average Change: ${Average}\n')
printWrite(f'Greatest Increase in Profits: {GreatIncreaseDate} ({GreatIncrease})\n')
printWrite(f'Greatest Decrease in Profits: {GreatDecreseDate} ({GreatDecrease})\n')

# output the result
