import os

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

all_bids = {}


def make_bid():
  winning_bid = 0
  winner = ""
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))

  all_bids[name] = bid
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'.")

  if more_bids == 'yes':
    os.system('cls')
    make_bid()
  else:
    os.system('cls')
    for key in all_bids:
      if all_bids[key] > winning_bid:
        winning_bid = all_bids[key]
        winner = key
    print(f"The winner of the bid is {winner} with a bid of ${winning_bid}!")

make_bid()
