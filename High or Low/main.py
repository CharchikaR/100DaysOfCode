from random import choice

from os import system

from art import logo, vs
from game_data import data


# Compare the followers
def check_answer(user_choice, followers_a, followers_b):
  if followers_a > followers_b:
    return user_choice == "a"
  else:
    return user_choice == "b"

def format_str(acc_data):
  '''Takes the account data and returns a formatted string'''
  name = acc_data["name"]
  desc = acc_data["description"]
  country = acc_data["country"]
  return f"{name}, {desc}, from {country}."

score = 0
play_again = True
# Generating random choice from the game data
rand_B = choice(data)

# Print the game art
print(logo)

while play_again:
  # Keeping the previous choice B as the A now
  rand_A = rand_B
  rand_B = choice(data)
  
  # Making sure rand_B choice is not the same as rand_A
  while rand_B == rand_A:
    rand_B = choice(data)
  
  # Printing the comparison A
  print(f"Compare A: {format_str(rand_A)}")
  
  # Print the vs logo
  print(vs)
  
  # Printing the comparison B
  print(f"Against B: {format_str(rand_B)}")
  
  # Ask User the input
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Followers Count
  followers_a = rand_A["follower_count"]
  followers_b = rand_B["follower_count"]
  
  # Check if user answer is correct or not
  is_correct = check_answer(user_choice, followers_a, followers_b)
  
  if is_correct:
    score +=1
    system("cls")
    print(f"You are right! Current score: {score}")
  else:
    play_again = False
    system("cls")
    print(f"Sorry that's not the correct answer! Final score: {score}")
