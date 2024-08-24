#Debugging Odd or Even: Day 13 Exercise 1

number = int(input("Which number do you want to check?"))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#As you can see the condition on line 5 should implicate the 'equivalence' to '0'
#Whereas it is implicating the 'assignment' of '0'.
#The Condition should be as mentioned below:
number % 2 == 0