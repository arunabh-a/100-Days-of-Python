# Debugging Leap Year: Day 13 Exercise 2

year = input("Which year do you want to check? ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#As you can see when taking input in line 3, we are asking for the year to be checked.
#We are dealing with numbers so it is adivsable to use integers as data types, but 
# the 'input()' function takes the values as strings by default, so the value stored in 'year' is a string. 
# We can Enclose the 'input()' with 'int()' function so it will return integers as values as mentioned below
int(input())