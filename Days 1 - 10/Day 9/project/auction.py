import os
import ui

print(ui.logo)
bids = {}

no_more = False

while no_more == False:
    name = input("Please Enter Your Name: ")
    bid = int(input(" How much you wish to Bid: ₹"))

    bids[name] = bid

    new_req = input("For New Entry, Type 'Yes' or to End, Type 'No' : ").lower()
    if new_req == "no":
        no_more = True
    else:
        os.system('CLS')
        os.system('clear')

highest = 0
winner = ""

for key in bids:
    bid_amnt = bids[key]
    if bid_amnt > highest:
        highest = bid_amnt
        winner = key
print (f" The Winner of this Auction is '{winner}' with the highest bid of '₹{highest}'")
