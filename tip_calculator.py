print("Welcome to the tip calculator!")

bill_amt = float(input("What was the total bill?"))

tip_amt = int(input("How much tip would you like to give? 10, 12, or 15?"))

people_amt = int(input("How many people to split the bill?"))

resulting_tip = (bill_amt * (tip_amt / 100) + bill_amt) / people_amt
print(f"Each person should pay: ${round(resulting_tip, 2)}")
