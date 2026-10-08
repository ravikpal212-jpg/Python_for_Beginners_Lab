text = input("Enter a string: ")
result = ""
new_word = True

# Convert the first character of every word to uppercase
# and the remaining alphabetic characters to lowercase.
for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch
        new_word = False
    else:
        if "A" <= ch <= "Z":
            result += chr(ord(ch) + 32)
        else:
            result += ch

print("Title case:", result)
