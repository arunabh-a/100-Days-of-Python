# Hurdle Challenge 4(Reeborg's World): Day 6 Exercise 4
# Note - The instructions in this program are in reference to the Reeborg's World Python Library (reeborg.ca)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_right():
    if right_is_clear() == True:
        turn_right()
        move() 
def manuever():
    if wall_in_front() == False:
        move()
    else:
        turn_left()
    if at_goal == False:
        while wall_on_right() and not wall_in_front():
            move()
    check_right()
    if wall_in_front() == True:
        check_right()
    elif wall_in_front() == False:
        check_right()

while not at_goal():
    manuever() 