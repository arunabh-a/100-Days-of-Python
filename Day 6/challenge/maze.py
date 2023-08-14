# Maze(Reeborg's World): Day 6 Final Challenge
# Note - The instructions in this program are in reference to the Reeborg's World Python Library (reeborg.ca)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()   

while not at_goal():
    if right_is_clear():
        turn_right()
        move()    
    elif front_is_clear():
        move()
    else:
        turn_left()
    
        