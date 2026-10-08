text = input("Enter a string: ")
count = 0
inside_word = False

# Count transitions from spaces to non-space characters.
for ch in text:
    if ch != " " and not inside_word:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words:", count)
