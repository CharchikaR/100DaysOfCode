from random import randint

from os import system

from art import logo, vs
from game_data import data

score = 0

def play_game(score):
  print(logo)
  # Generating random choice 
  rand_A = randint(0, len(data) - 1)
  rand_B = rand_A
  
  # Making sure rand_B choice is not the same as rand_A
  while rand_B == rand_A:
    rand_B = randint(0, len(data) - 1)
  
  # Printing the comparison A
  print(f"Compare A: {data[rand_A]['name']}, {data[rand_A]['description']}, from {data[rand_A]['country']}.")
  
  # Print the vs logo
  print(vs)
  
  # Printing the comparison B
  print(f"Against B: {data[rand_B]['name']}, {data[rand_B]['description']}, from {data[rand_B]['country']}.")
  
  # Compare the followers
  followers_A = data[rand_A]["follower_count"]
  followers_B = data[rand_B]["follower_count"]
  # for testing -> print(followers_A, followers_B)

  # Ask User the input
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user answer is correct or not
  if user_choice == "a":
    if followers_A > followers_B:
      score += 1
      system('cls')
      print(f"You're right! Current score: {score} ")
      play_game(score)
      
    else:
      print(f"Sorry that's wrong! Final score: {score}")
  elif user_choice == "b":
    if followers_B > followers_A:
      score += 1
      system('cls')
      print(f"You're right! Current score: {score} ")
      play_game(score)
    else:
      system('cls')
      print(f"Sorry that's wrong! Final score: {score}")
  
play_game(score)