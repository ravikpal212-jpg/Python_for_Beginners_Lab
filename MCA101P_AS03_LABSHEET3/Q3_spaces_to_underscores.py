text = input("Enter a string: ")
result = ""

# Replace each space manually.
for ch in text:
    if ch == " ":
        result += "_"
    else:
        result += ch

print("Result:", result)
