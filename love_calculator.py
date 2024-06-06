print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

names = (name1 + name2).lower()
true = 0
love = 0
t_count = names.count("t")
r_count = names.count("r")
u_count = names.count("u")
e_count = names.count("e")

true += t_count + r_count + u_count + e_count

l_count = names.count("l")
o_count = names.count("o")
v_count = names.count("v")
e_count = names.count("e")

love += l_count + o_count + v_count + e_count

love_scores = int(str(true) + str(love))

if love_scores <= 10 or love_scores >=90:
  print(f"Your score is {love_scores}, you go together like coke and mentos.")
elif love_scores >=40 and love_scores <= 50:
  print(f"Your score is {love_scores}, you are alright together.")
else:
  print(f"Your score is {love_scores}.")
