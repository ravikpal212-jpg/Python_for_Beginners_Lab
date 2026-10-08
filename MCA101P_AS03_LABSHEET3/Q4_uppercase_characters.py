text = input("Enter a string: ")
result = ""

# Extract uppercase alphabetic characters.
for ch in text:
    if "A" <= ch <= "Z":
        result += ch

print("Uppercase characters:", result)
