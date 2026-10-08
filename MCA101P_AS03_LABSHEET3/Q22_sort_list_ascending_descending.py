items = input("Enter integers separated by spaces: ").split()
numbers = []

for item in items:
    numbers.append(int(item))

# Bubble sort in ascending order.
n = len(numbers)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        j += 1
    i += 1

print("Ascending order:", numbers)

# Print the same sorted list in reverse order without reverse().
print("Descending order:", end=" ")
i = len(numbers) - 1
while i >= 0:
    print(numbers[i], end=" ")
    i -= 1
print()
