#Paint Area Calculator: Day 8 Exercise 1
import math
def paint_calc(height, width, cover):
    area = height * width
    numcans = math.ceil(area / cover)
    print(f"You'll need {numcans} cans of paint.")
    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

