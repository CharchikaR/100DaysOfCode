import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Taking the player's input
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
players_choice = int(input(" "))

# The choices available for 0 , 1 , 2
choices = [rock, paper, scissors]

# Printing the player's choice
if players_choice >= 3 or players_choice < 0:
    print("Invalid number input!")
else:
    print("You chose: ")
    print(choices[players_choice])

    # Randomising AI choice:
    ai_choice = random.randint(0, 2)

    # Printing the AI Choice:
    print("AI chose:")
    print(choices[ai_choice])

    # Determining the outcome:
    # 0 > 2 , 2 > 1 , 1 > 0

    if players_choice == 0 and ai_choice == 2:
        print("You Win!")
    elif players_choice == 2 and ai_choice == 1:
        print("You Win!")
    elif players_choice == 1 and ai_choice == 0:
        print("You Win!")
    elif players_choice == 0 and ai_choice == 1:
        print("You Lose!")
    elif players_choice == 1 and ai_choice == 2:
        print("You Lose!")
    elif players_choice == 2 and ai_choice == 0:
        print("You Lose!")
    else:
        print("Draw!")