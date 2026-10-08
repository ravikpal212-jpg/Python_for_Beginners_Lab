text = input("Enter a string: ")
reversed_text = ""

# Build the reversed string from right to left.
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1

print("Reversed string:", reversed_text)
