# FizzBuzz: Day 5 Exercise 4
for num in range (1, 101):
    if num % 3 == 0 and num % 5 ==0:
        num = "FizzBuzz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0:
        num = "Fizz" 
        
    print(num)