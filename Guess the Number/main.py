from art import logo
import random

print(logo)

print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n"
)

level = input("Choose a difficulty mode. Type 'easy' or 'hard': ").lower()
chances = 0

if level == "easy":
    chances = 10
else:
    chances = 5

print(f"You have {chances} attempts to guess the number!\n")
target_number = random.randint(1,101)
#print(f"psst! the answer is : {target_number}")

while chances > 0:
  guessed_number = int(input("Make a guess: "))
 
  if guessed_number == target_number: 
    print(f"You guessed it! The correct answer is {target_number}")
    break
  else:
    chances -= 1
    if guessed_number > target_number:
      guess = "too high"
    else:
      guess = "too low"
    if chances == 0:
      print("You've run out of attempts, You lose!")
      break
    print(f"Oops! Your guess is {guess}! You have now {chances} attempts left!")

