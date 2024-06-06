# 1st input: enter height in meters e.g: 1.65
height = input("Please enter your height in meters (e.g: 1.65): ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Please enter weight in kilograms (e.g: 72): ")

height_num = float(height)
weight_num = int(weight)

bmi = (weight_num)/(height_num)**2
bmi_whole = int(bmi)

print(f"Your bmi is {bmi_whole}")