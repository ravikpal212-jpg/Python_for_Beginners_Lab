first = input("Enter the first string: ")
second = input("Enter the second string: ")

# Two strings are rotations if they have the same length
# and the second occurs inside first + first.
is_rotation = False

if len(first) == len(second):
    combined = first + first
    start = 0
    while start <= len(combined) - len(second):
        match = True
        j = 0
        while j < len(second):
            if combined[start + j] != second[j]:
                match = False
                break
            j += 1
        if match:
            is_rotation = True
            break
        start += 1

if is_rotation:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
