text = input("Enter the main string: ")
substring = input("Enter the substring: ")

# Search for the substring without using the 'in' operator.
found = False

if len(substring) == 0:
    found = True
else:
    start = 0
    while start <= len(text) - len(substring):
        match = True
        j = 0
        while j < len(substring):
            if text[start + j] != substring[j]:
                match = False
                break
            j += 1
        if match:
            found = True
            break
        start += 1

if found:
    print("Substring exists in the string.")
else:
    print("Substring does not exist in the string.")
