from art import *
import os

bidding_over = False
bidders = {}
highest_bid = 0
winner_name = ""
print(logo)

print("Welcome to the Secret Auction!\n")

while(bidding_over == False):
    get_name = input("What is your name? ")
    get_bid = input("How much do you want to bid? $")

    bidders[get_name] = int(get_bid)

    other_bidder = input("Is there another bidder? Type 'yes' to add them, type 'no' to end bidding: ")
    if(other_bidder == "no"):
        break
    else:
        os.system('clear')


for key in bidders:
    if(bidders[key] > highest_bid):
        highest_bid = bidders[key]
        winner_name = key
    elif(bidders[key] == highest_bid):
        print("There is a tie please start over")


print(f"The auction is over. The winner is {winner_name} with a bid of {highest_bid}")