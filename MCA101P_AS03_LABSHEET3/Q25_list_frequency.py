items = input("Enter list elements separated by spaces: ").split()
frequency = {}

# Count occurrences of every list element.
for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Element frequencies:")
for item in frequency:
    print(item, ":", frequency[item])
