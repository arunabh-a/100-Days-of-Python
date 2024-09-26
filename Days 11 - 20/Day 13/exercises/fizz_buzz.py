for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# There are Multiple Issues to Deal With, which are as follows:
#   In Line 2, we need both conditions to be true but the logical 
#   operator 'or' executes the statements even if one of the condition is true.
#   We need to use 'and' operator for the situation as mentioned below
    number % 3 == 0 and number % 5 == 0 

#   In Line 9, the values of 'number' are getting printed as single-element lists.
#   This is unnecessary as we are dealing with numbers so we could 
#   print the values as integers as mentioned below\
    print(number)

#   In Lines 6, 8 and 10, we are 'printing' strings with respect to the conditions mentioned
#   but we are supposed to 'replace' the integer we are currently looping through with a string.
#   We need to reiterate the value of 'number' so it replaces the integer as mentioned below
    num = "Fizz"