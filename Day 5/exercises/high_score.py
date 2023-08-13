# High Score: Day 5 Exercise 2
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

largest_num = 0 
for num in student_scores:
    if num > largest_num:
        largest_num = num

print (f"The highest score in the class is: {largest_num}")
