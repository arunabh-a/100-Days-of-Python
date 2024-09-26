# BMI Calculator: Day 2 Exercise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h = float(height)
w = float(weight)
bmi = w / h**2
print(round(bmi))