print("\n" * 100)
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Blind Auction ! ")

highest_bid = 0
winner = ""
bids = {}


def bidding(records):
    highest_bid = 0
    winner = ""
    for bidder in records:
        bid_rn = records[bidder]
        if bid_rn > highest_bid:
            winner = bidder
            highest_bid = bid_rn
    print(f"The winner is {bidder} with a winning bid of ${highest_bid}.")


repeat = True
while repeat:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bids[name] = bid
    again = input("Are there any more users? Type 'yes' or 'no': ").lower()
    if again == 'no':
        repeat = False
        print("\n" * 100)
        bidding(bids)
    elif again == 'yes':
        print("\n" * 100)