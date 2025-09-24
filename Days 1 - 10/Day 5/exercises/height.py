# Average Height: Day 5 Exercise 1
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

heightsum = 0
heightlen = 0
for h in student_heights:
    heightsum += h
    heightlen = n + 1

average = round(heightsum/heightlen)

print(average)



