# Hurdle Challenge 1(Reeborg's World): Day 6 Exercise 1
# Note - The instructions in this program are in reference to the Reeborg's World Python Library (reeborg.ca)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def manuever():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    manuever()