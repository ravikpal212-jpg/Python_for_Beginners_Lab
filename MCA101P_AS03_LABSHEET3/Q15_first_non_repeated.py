text = input("Enter a string: ")
frequency = {}

# Count occurrences of every character.
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

first = None
for ch in text:
    if frequency[ch] == 1:
        first = ch
        break

if first is not None:
    print("First non-repeated character:", first)
else:
    print("No non-repeated character found.")
