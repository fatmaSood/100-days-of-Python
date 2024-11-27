import os
from art import logo


def clear_console():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


print(logo)
other_bid = True
bids = {}  # initiate an empty dict

while other_bid:
    print('Welcome to the secret auction program.')
    name = input("What is your name?:")
    bid = float(input("What's your bid?: "))  # Convert bid to float for numerical comparison
    bids[name] = bid  # key is the name and the value is the bid

    again = input("Are there any other bidders? Type 'yes' or 'no': ").lower()  # Normalize input to lowercase
    if again == "yes":
        clear_console()  # Clear the console if there are more bidders
    else:
        other_bid = False  # Exit the loop if no more bidders

# Determine the highest bid
if bids:
    highest_bidder = max(bids, key=bids.get)  # Get the name of the highest bidder
    highest_bid = bids[highest_bidder]  # Get the highest bid amount
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid:.2f}!")
else:
    print("No bids were placed.")
