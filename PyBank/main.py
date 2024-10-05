# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_losses = None
changes = []
dates = []
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


        # Track the total number of months
    total_months += 1    

    # Process each row of data
    for row in reader:
        date = row[0]
        profit_losses = int(row[1])

        # Track the total
    total_months += 1

        # Track the net change
    net_total += profit_losses

        # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
        # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]


# Calculate the average net change across the months
average_change = sum(changes) / len(changes)


# Generate the output summary

# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# Write the results to a text file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")