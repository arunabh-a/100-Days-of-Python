#Prime Numbers: Day 8 Exercise 2
def prime_checker(number):
    primecheck = True
    for num in range (2, number):
        if number % num == 0:
            primecheck = False
    if primecheck == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number = n)
