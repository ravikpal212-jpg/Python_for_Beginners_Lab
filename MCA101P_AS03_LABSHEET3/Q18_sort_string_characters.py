text = input("Enter a string: ")
characters = []

# Copy characters into a list.
for ch in text:
    characters.append(ch)

# Bubble sort characters alphabetically.
n = len(characters)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if characters[j].lower() > characters[j + 1].lower():
            temp = characters[j]
            characters[j] = characters[j + 1]
            characters[j + 1] = temp
        j += 1
    i += 1

result = ""
for ch in characters:
    result += ch

print("Characters in alphabetical order:", result)
