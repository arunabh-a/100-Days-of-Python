# Hurdle Challenge 3(Reeborg's World): Day 6 Exercise 3
# Note - The instructions in this program are in reference to the Reeborg's World Python Library (reeborg.ca)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def manuever():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        manuever()
    else:
        move()
