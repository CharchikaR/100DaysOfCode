
def prime_checker(number):
    isPrime = False
    for x in range(2, number):
      if number % x == 0:
        isPrime = False
        break
      else: 
        isPrime = True
    if isPrime:
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")

n = int(input("Enter any natural number to check if it's prime: ")) 

prime_checker(number=n)