#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

ez_pass = []
for x in range(1, nr_letters + 1):
    rand_letter = letters[random.randint(0, len(letters) - 1)]
    ez_pass.append(rand_letter)
for x in range(1, nr_symbols + 1):
    rand_symbol = symbols[random.randint(0, len(symbols) - 1)]
    ez_pass.append(rand_symbol)
for x in range(1, nr_numbers + 1):
    rand_num = numbers[random.randint(0, len(numbers) - 1)]
    ez_pass.append(rand_num)
print(ez_pass)

hard_pass = ez_pass[:]
random.shuffle(hard_pass)
print(hard_pass)

print(f"Your password is: {''.join(hard_pass)}")
