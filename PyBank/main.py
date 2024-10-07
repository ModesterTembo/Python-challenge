# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("C:\\Users\\LENOVO\\OneDrive\\Bootcamp\\Python-challenge\\PyBank\\Resources\\budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    net_total += int(first_row[1])
    previous_profit = int(first_row[1])

    # Process each row of data
    for row in reader:
        date = row[0]
        profit_losses = int(row[1])

        # Track the total
        total_months += 1

        # Track the net change
        net_total += profit_losses

        # Calculate changes in "Profit/Losses"
        if previous_profit is not None:
            change = profit_losses - previous_profit
            changes.append(change)
            dates.append(date)
        previous_profit = profit_losses

# Calculate the greatest increase and decrease in profits
if changes:
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]
    average_change = sum(changes) / len(changes)

    # Generate the output summary
    summary = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    )

    # Print the output
    print(summary)

    # Write the results to a text file
    with open(file_to_output, 'w') as txtfile:
        txtfile.write(summary)
else:
    print("No changes in Profit/Losses to analyze.")