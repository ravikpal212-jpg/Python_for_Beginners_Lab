first = input("Enter first list elements separated by spaces: ").split()
second = input("Enter second list elements separated by spaces: ").split()
common = []

# Find common elements without using set().
for item in first:
    present = False
    for value in second:
        if item == value:
            present = True
            break

    if present:
        already_added = False
        for value in common:
            if value == item:
                already_added = True
                break
        if not already_added:
            common.append(item)

print("Common elements:", common)
