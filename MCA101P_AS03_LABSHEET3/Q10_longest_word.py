text = input("Enter a string: ")
current = ""
longest = ""

# Find the longest word without split().
for ch in text + " ":
    if ch != " ":
        current += ch
    else:
        if len(current) > len(longest):
            longest = current
        current = ""

print("Longest word:", longest)
