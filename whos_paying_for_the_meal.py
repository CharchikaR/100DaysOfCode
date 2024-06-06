import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

list_length = len(names)
person = names[(random.randint(0,(list_length - 1)))]
print(f"{person} is going to buy the meal today!")