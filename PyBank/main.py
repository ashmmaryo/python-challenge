import os
import csv

#variables
months = []
profit_loss_changes = []
month_count = 0 
current_month_profit_loss = 0 
total_profit_loss = 0 
previous_month_profit_loss = 0
total_profit_loss_change = 0 
change_count = 0
first_row = True

#import and open source file 
bd_csv = os.path.join("Resources", "budget_data.csv")

with open(bd_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
#loop through csv to find total number of months
    for row in csv_reader:
        month_count +=1

        #total profit/loss     
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        #change in profit/loss between current and previous months
        if first_row:    
            first_row = False   
        else: 
            change_count +=1
            current_profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            total_profit_loss_change += current_profit_loss_change
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            #create lists for profit loss changes and months
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

            #find greatest increase/decrease in profits
            greatest_increase_profit_loss = max(profit_loss_changes)
            greatest_decrease_profit_loss = min(profit_loss_changes)

            #find month that matches greatest increase/decrease in profits           
            greatest_increase_month = profit_loss_changes.index(greatest_increase_profit_loss) 
            greatest_decrease_month = profit_loss_changes.index(greatest_decrease_profit_loss) 
            highest_month = months[greatest_increase_month]
            lowest_month = months[greatest_decrease_month]

        #hold current month profit loss for next loop
        previous_month_profit_loss = current_month_profit_loss

    #find the average change in profit/loss between current and previous months
    ave_profit_loss_change = round(total_profit_loss_change / change_count, 2)

    #print analysis report
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${ave_profit_loss_change}")
    print(f"Greatest Increase in Profits: {highest_month } ${greatest_increase_profit_loss}")
    print(f"Greatest Decrease in Profits: {lowest_month } ${greatest_decrease_profit_loss}")

    
#output file to Analysis folder
output_file = os.path.join("Analysis", "Final_Analysis.txt")
with open(output_file, "w") as results:

#write analysis report to txt file
    results.write("Financial Analysis\n")
    results.write("-------------------------------\n")
    results.write(f"Total Months: {month_count}\n")
    results.write(f"Total: ${total_profit_loss}\n")
    results.write(f"Average Change: ${ave_profit_loss_change}\n")
    results.write(f"Greatest Increase in Profits: {highest_month } ${greatest_increase_profit_loss}\n")
    results.write(f"Greatest Decrease in Profits: {lowest_month } ${greatest_decrease_profit_loss}\n")   