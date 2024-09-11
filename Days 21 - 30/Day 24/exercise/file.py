# File Handling: Day 24

with open("text-file.txt", "w+") as file:
    file.write("\n This is test file written by this script")
    print(file.read())