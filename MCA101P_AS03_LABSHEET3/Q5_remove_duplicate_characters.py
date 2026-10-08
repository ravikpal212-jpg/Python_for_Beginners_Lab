text = input("Enter a string: ")
result = ""

# Keep only the first occurrence of each character.
for ch in text:
    found = False
    for existing in result:
        if ch == existing:
            found = True
            break
    if not found:
        result += ch

print("After removing duplicates:", result)
