# Code was written in a replit environment
from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

# Start
print(logo)
bidder = input("What is your name?: \n")
# print(bidder)
bid = int(input("What is your bid?: \n$"))
# print(f"${bid}")

# create a dictionary
bidding_list = {}
bidding_list[bidder] = bid

# check if there are other bidders
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
# if yes, clear the screen and ask for the next bidder
while other_bidders == "yes":
    clear()
    bidder = input("What is your name?: \n")
    # print(bidder)
    bid = int(input("What is your bid?: \n$"))
    # print(f"${bid}")
    bidding_list[bidder] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

# if no, find the highest bid in the dictionary and declare them as the winner
if other_bidders == "no":
    clear()
    print(logo)
    highest_bid = 0
    for bidder in bidding_list:
        if bidding_list[bidder] > highest_bid:
            highest_bid = bidding_list[bidder]
            winner = bidder
    print(f"The number of bids receieved is {len(bidding_list)}, and the winner is {
          winner} with a bid of ${highest_bid}.")
