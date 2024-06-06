# Which year do you want to check?
year = int(input())

isLeap = True

if year%4 == 0:
  if year%100 == 0:
    isLeap = False
    if year%400 == 0:
      isLeap = True 
else:
  isLeap = False


if isLeap:
  print("Leap year")
else: 
  print("Not leap year")