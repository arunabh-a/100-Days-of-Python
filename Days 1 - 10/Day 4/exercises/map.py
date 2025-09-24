# Treasure Map: Day 4 Exercise 3

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

coords = position.split()
horizontal = int(position[0])
vertical = int(position[1])


row = map[vertical - 1] # referencing the selected row mentioned in line 6
row[horizontal -1] = "X" # referencing the selected column 'inside' the 'selected row' in line 15


print(f"{row1}\n{row2}\n{row3}")

# 0 wins over 2 
# 2 wins over 1
# 1 wins over 0