# List Slicing: Day 21 Exercise


Lst = [50, 70, 30, 20, 90, 10, 50]

# Display list
print("List Lst[-7::1]:")
print(Lst[-7::1])
print()

# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print("List[3:9:2]:")
print(List[3:9:2])

# Display sliced list
print("List[::2]:")
print(List[::2])

# Display sliced list
print("List[::]:")
print(List[::])
print()

# Initialize list
List = ['Example', 4, 'Sample']

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print("List[::-1]:")
print(List[::-1])

# Display sliced list
print("List[::-3]:")
print(List[::-3])

# Display sliced list
print("List[:1:-2]:")
print(List[:1:-2])
print()

# Initialize list
List = [-999, 'ABC', 1706256, '^_^', 3.1496]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print("List[10::2]:")
print(List[10::2])

# Display sliced list
print("List[1:1:1]:")
print(List[1:1:1])

# Display sliced list
print("List[-1:-1:-1]:")
print(List[-1:-1:-1])

# Display sliced list
print("List[:0:]:")
print(List[:0:])
print()

# Initialize list
List = [-999, 'XYZ', 1706256, 3.1496, '^_^']

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Modified List
List[2:4] = ['Item1', 'Item2', 'Item3', 'Item4']

# Display sliced list
print("List after modification (List[2:4] = ['Item1', 'Item2', 'Item3', 'Item4']):")
print(List)

# Modified List
List[:6] = []

# Display sliced list
print("List after modification (List[:6] = []):")
print(List)
print()

# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("Original List:\n", List)

print("\nSliced Lists: ")

# Creating new List
newList = List[:3] + List[7:]

# Display sliced list
print("New List (List[:3] + List[7:]):")
print(newList)

# Changing existing List
List = List[::2] + List[1::2]

# Display sliced list
print("List after modification (List[::2] + List[1::2]):")
print(List)
