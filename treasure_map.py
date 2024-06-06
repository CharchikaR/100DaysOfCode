line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure (enter coords like B3)?: ") 

coord_1 = 0
coord_2 = 0

if position[1] == "1":
  if position[0] == "A":
    coord_2 = 0
  elif position[0] == "B":
    coord_2 = 1
  else: 
    coord_2 = 2
elif position[0] =="2":
  coord_1 = 1
  if position[0] == "A":
    coord_2 = 0
  elif position[0] == "B":
    coord_2 = 1
  else: 
    coord_2 = 2
else: 
  coord_1 = 2
  if position[0] == "A":
    coord_2 = 0
  elif position[0] == "B":
    coord_2 = 1
  else: 
    coord_2 = 2

map[coord_1][coord_2] = 'X'

print(f"{line1}\n{line2}\n{line3}")