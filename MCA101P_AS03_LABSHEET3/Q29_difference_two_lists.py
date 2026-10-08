first = input("Enter first list elements separated by spaces: ").split()
second = input("Enter second list elements separated by spaces: ").split()
difference = []

# Find elements present in the first list but not in the second.
for item in first:
    present = False
    for value in second:
        if item == value:
            present = True
            break

    if not present:
        already_added = False
        for value in difference:
            if value == item:
                already_added = True
                break
        if not already_added:
            difference.append(item)

print("Difference (first list - second list):", difference)
