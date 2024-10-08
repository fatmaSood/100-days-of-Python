# If the bill was $150.00, split between 5 people, with 12% tip.
import math

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to tip calculator.")
total_bill = float(input("What was the total bill? \n"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill? \n"))

perc_total = (total_bill * (percentage / 100))
new_bill = (perc_total + total_bill) / people
final_amt = round(new_bill, 2)
print(f"Each person should pay: {final_amt}")
