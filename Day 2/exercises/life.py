# Life in Weeks: Day 2 Exercise 3
age = input("What is your current age? ")

year = 90 - int(age)
month = 12 * year 
week = 52 * year
day = 365 * year
print(f'You have {day} days, {week} weeks, and {month} months left.')
#The above mentioned string is an F String