import random
from os import system

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
       
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Use this function to deal a random card
def deal_cards():
  card = random.choice(cards)
  return card

# Use this function to calculate the sum of a set of cards
def calc_score (cards):
  score = 0
  for x in cards:
   score += x
  return score

# Show hands
def show_hands_final(user_score, computer_score):
  print(f"Your final hand: {user_cards} Score: {user_score}\nComputer's final hand: {computer_cards} Computer Score: {computer_score}")

def show_hands(user_score):
  print(f"Your cards: {user_cards} Current score: {user_score}\nComputer's first cards: {computer_cards[0]}")


def blackjack(user_score, computer_score):
  
  # Calculate score and save them
    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)
    
    # Check for Blackjack
    if user_score == 21:
      if computer_score != 21: 
        show_hands_final(user_score, computer_score)
        print("Blackjack! You win! 🎉")
        return
      else:
        show_hands_final(user_score, computer_score)
        print("Draw!")
        return
    else: 
      if user_score > 21:
        if 11 in user_cards:
          user_cards[user_cards.index(11)] = 1
          user_score = calc_score(user_cards)
          if user_score > 21: 
            show_hands_final(user_score, computer_score)
            print("Bust! You went over! 😵 ")
            return
            
        else:
          show_hands_final(user_score, computer_score)
          print("Bust! You went over! 😵 ")
          return
          
      else:
        show_hands(user_score, computer_score)
        deal_another = input("Do you want another card? (y/n)")
        if deal_another == 'y':
          #Deal cards to the user 
          user_cards.append(deal_cards())
          blackjack(user_score, computer_score)
        else:
          while computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = calc_score(computer_cards)
          if computer_score > 21:
            show_hands_final(user_score, computer_score)
            print("The computer went over! You win! 😬")
            return
          else:     
            if computer_score > user_score: 
              show_hands_final(user_score, computer_score)
              print("You lose! ☠️")
              return
            elif computer_score < user_score:
              show_hands_final(user_score, computer_score)
              print("You win! 🎉")
              return
            else: 
              show_hands_final(user_score, computer_score)
              print("It's a Draw! 🫣")
              return

# Take the input to start the game 
play_game = input("Do you want to play blackjack? (y/n)")
while play_game == "y":
  system('cls')
  print(logo)
  user_cards = []
  computer_cards = []
  user_score = 0
  computer_score = 0
  deal_another = 'y'
  
  #Deal 2 cards to user and computer
  user_cards.append(deal_cards())
  user_cards.append(deal_cards())
  computer_cards.append(deal_cards())
  computer_cards.append(deal_cards())
  
  blackjack(user_score, computer_score)    
  play_game = input("Do you want to play blackjack? (y/n)")