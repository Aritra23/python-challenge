import os
import csv

pybank_csv_path = os.path.join("budget_data.csv")

file_output = "results.txt"

#Default variable initialization
total_months = 0
total_profit_losses = 0
prev_profit_losses = 0
month_of_change = []
profit_change_list = []
biggest_decr_losses = ['', 99999999999]
biggest_incr_profit = ['', 0]

with open(pybank_csv_path,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Count the total of months
        total_months += 1
        #Calculate the total profit over the entire period
        total_profit_losses += int(row['Profit/Losses'])

        #Calulate the average change in profit/losses change between months over the entire period
        profit_change = int(row["Profit/Losses"])- prev_profit_losses
        prev_profit_losses = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change + [row["Date"]]
        #The greatest increase in profit (date and amount) over the entire period
        if profit_change>biggest_incr_profit[1]:
            biggest_incr_profit[1]= profit_change
            biggest_incr_profit[0] = row['Date']
        #The greatest decrease in losses (date and amount) over the entire period
        if profit_change<biggest_decr_losses[1]:
            biggest_decr_losses[1]= profit_change
            biggest_decr_losses[0] = row['Date']


rev_avg = sum(profit_change_list)/len(profit_change_list)



print("Total Months: " + str(total_months))
print("Total Profit/Losses: $ " + str(total_profit_losses))
print('Average Change in Profit/Losses: $ ' + str(rev_avg))
print("The greatest increase in profits (date and amount) over the entire period: " +str(biggest_incr_profit[0]) + " "+str(biggest_incr_profit[1]))
print("The greatest decrease in losses (date and amount) over the entire period: "+str(biggest_decr_losses[0]) + " "+str(biggest_decr_losses[1]))



with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Profits/Losses: $%d\n" % total_profit_losses)
    file.write("Average Change in Profit/Losses: $%d\n" % rev_avg)
    file.write("Greatest Increase in Profit: %s ($%s)\n" % (biggest_incr_profit[0], biggest_incr_profit[1]))
    file.write("Greatest Decrease in Losses: %s ($%s)\n" % (biggest_decr_losses[0], biggest_decr_losses[1]))