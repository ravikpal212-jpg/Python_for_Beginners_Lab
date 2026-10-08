text = input("Enter a string: ")

# Print every non-empty substring.
print("All substrings:")
start = 0
while start < len(text):
    end = start + 1
    while end <= len(text):
        print(text[start:end])
        end += 1
    start += 1
