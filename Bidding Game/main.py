import os
from art import logo


print(logo)
bids={}
bidding_finished=False

def highest_bid(bidding_record):
  highest_bid = 0
  winner=""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid = bid_amount
      winner=bidder
      
  print(f"The winner is {winner} with a bid of ${highest_bid}")  
while not bidding_finished:
  bidder_name =input("What is your name?: ")
  bid_amount=int(input("What is your bid? $"))
  bids[bidder_name] = bid_amount
  bid_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bid_continue.lower()
  if bid_continue == "no":
    bidding_finished = True
    highest_bid(bids)
  elif bid_continue =="yes":
    os.system('cls')

