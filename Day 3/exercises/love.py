# Love Calculator: Day 3 Exercise 5
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1 + name2
lower_combined = combined.lower()

t = lower_combined.count('t') 
r = lower_combined.count('r') 
u = lower_combined.count('u') 
e = lower_combined.count('e') 
true = t+r+u+e
l = lower_combined.count('l') 
o = lower_combined.count('o') 
v = lower_combined.count('v') 
e = lower_combined.count('e') 
love = l+o+v+e

total = int(str(true) + str(love))

if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) or (total <=50) or (total == 54):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")