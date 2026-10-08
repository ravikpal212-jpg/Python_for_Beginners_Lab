items = input("Enter list elements separated by spaces: ").split()
result = []

# Add an element only if it has not appeared before.
for item in items:
    found = False
    for existing in result:
        if item == existing:
            found = True
            break
    if not found:
        result.append(item)

print("List without duplicates:", result)
