from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("")
print("Welcome to the Secret Auction!")
print("")

bid_roll = {}
highest = 0
name = ""

def auction(name, bid):
    bid_roll[name] = bid

bidding = True

while bidding:
  their_name = input("Your Name: ")
  their_bid = int(input("Your Bid: $"))
  
  auction(their_name, their_bid)
    
  print("")
  more_bids = input("Anymore bids? Yes or No\n").lower()
    
  if more_bids == "yes":
    clear()
    print(logo)
  if more_bids == "no":
    bidding = False
    for bidder in bid_roll:
        if bid_roll[bidder] > highest:
            highest = bid_roll[bidder]
        
        if bid_roll[bidder] == highest:
            name = bidder
    clear()
    print(f"The winner is {name} with a bid of ${highest}!")
    #print(bid_roll)
