items = input("Enter list elements separated by spaces: ").split()
reversed_list = []

# Traverse from the last index to the first.
index = len(items) - 1
while index >= 0:
    reversed_list.append(items[index])
    index -= 1

print("Reversed list:", reversed_list)
