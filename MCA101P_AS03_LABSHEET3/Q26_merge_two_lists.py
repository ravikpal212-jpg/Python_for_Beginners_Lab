first = input("Enter first list elements separated by spaces: ").split()
second = input("Enter second list elements separated by spaces: ").split()

merged = []

# Append elements from both lists manually.
for item in first:
    merged.append(item)

for item in second:
    merged.append(item)

print("Merged list:", merged)
