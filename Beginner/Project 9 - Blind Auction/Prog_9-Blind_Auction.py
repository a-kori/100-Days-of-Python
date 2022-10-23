import resources
import time

resources.clear()
print(resources.auction_logo)
print("Welcome to the Blind Auction program!\n")
time.sleep(5)

auction = {}
while True :
    resources.clear()
    print(resources.auction_logo)
    name = input("What is your name? ")
    
    while True :
        try :
            bid = abs(int(input("\nWhat's your bid? $")))
            break
        except :
            print("Seems like you've entered a non-numeric value as a bid. Try again.")

    auction[name] = bid

    print("\nAre there any other bidders?", end = " ")
    if input("Type 'y' for yes or anything else for no: ") != "y" :
        print()
        break

max_bid = 0
max_bidder = ""

for bidder in auction :
    bid = auction[bidder]
    if bid > max_bid :
        max_bid = bid
        max_bidder = bidder

resources.clear()
print(resources.auction_logo)
print(f"The winner is {max_bidder} with a bid of ${max_bid}.\n")