text = input("Enter a string: ")
frequency = {}

# Count each character manually using a dictionary.
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequencies:")
for ch in frequency:
    print(repr(ch), ":", frequency[ch])
