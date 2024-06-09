
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply 
def multiply(n1, n2):
  return n1 * n2

# Divide 
def divide(n1, n2):
  return n1 / n2

# Storing the functions 
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calc():
 
  num1 = float(input("What's the first number? : "))
  for operand in operations:
    print(operand)
  should_continue = True
  
  while should_continue:
    op = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? : "))
    ans = operations[op](num1, num2)
    
    print(f"{num1} {op} {num2} = {ans}")
    
    carry_on = (input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit and start a new calculation : ")).lower()
    if carry_on == "y":
      num1 = ans
    else:
      should_continue = False
      calc()    
calc()