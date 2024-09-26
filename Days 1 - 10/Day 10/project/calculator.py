# Calculator : Day 10 Project
import ui
print(ui.logo)
def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

operations = {
    "+" : add,
    "-" : sub,
    "x" : mul,
    "/" : div,
}

def calculation():
    a = float(input("Enter the First Number : "))

    print("Available Options:-")
    for key in operations:
        print(key) 

    continued = True
    while continued == True:
        choice_op = input("Choose an Operation : ")
        b = float(input("Enter the Second Number : "))

        opinit = operations[choice_op]
        answer = opinit(a, b)

        print(f"{a} {choice_op} {b} = {answer}")
        reitr = input("Type 'over' to calculate over or 'fresh' to start a fresh calculation\n").lower()
        if reitr == "over":
            a = answer
        elif reitr == "fresh":
            calculation()
        else:
            continued = False

calculation()




