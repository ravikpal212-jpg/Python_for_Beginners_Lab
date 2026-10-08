text = input("Enter a string: ")
words = []
current = ""

# Extract words manually.
for ch in text + " ":
    if ch != " ":
        current += ch.lower()
    else:
        if current != "":
            words.append(current)
            current = ""

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_word = None
highest = 0
for word in frequency:
    if frequency[word] > highest:
        highest = frequency[word]
        most_word = word

if most_word is not None:
    print("Most repeated word:", most_word)
    print("Frequency:", highest)
else:
    print("No words found.")
