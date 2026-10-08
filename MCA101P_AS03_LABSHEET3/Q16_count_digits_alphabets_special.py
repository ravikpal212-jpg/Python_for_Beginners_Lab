text = input("Enter a string: ")
digits = 0
alphabets = 0
special = 0

# Classify each character.
for ch in text:
    if "0" <= ch <= "9":
        digits += 1
    elif ("a" <= ch.lower() <= "z"):
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters:", special)
