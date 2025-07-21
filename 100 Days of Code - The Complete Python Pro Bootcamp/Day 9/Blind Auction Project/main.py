import art
print(art.logo)
bid_dictionary= { }
# TODO-1: Ask the user for input
print("Welcome to the secret auction program")

def bid():
    name = input("What is your name: ")
    bid_value = int(input("Enter your bid: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_dictionary[name] = bid_value

# TODO-4: Compare bids in dictionary
def highest_bidder():
    max_bid = 0
    bidder_name = ""
    for bidders in bid_dictionary:
        if bid_dictionary[bidders] > max_bid:
            max_bid = bid_dictionary[bidders]
            bidder_name = bidders

    print(f"The winner is {bidder_name} with a bid of ${max_bid}")

# TODO-3: Whether if new bids need to be added
new_bid = True
while new_bid:
    bid()
    next_bidder = input("Are there other bidders? Type 'yes' or 'no':\n")
    if next_bidder == "no":
        new_bid = False
        highest_bidder()
    else:
        print("\n" * 20)



