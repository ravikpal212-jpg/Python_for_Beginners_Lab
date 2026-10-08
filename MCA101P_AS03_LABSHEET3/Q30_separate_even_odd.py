items = input("Enter integers separated by spaces: ").split()
even = []
odd = []

# Separate numbers according to divisibility by 2.
for item in items:
    number = int(item)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)
