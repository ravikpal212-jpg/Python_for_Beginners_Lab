items = input("Enter integers separated by spaces: ").split()
numbers = []

for item in items:
    numbers.append(int(item))

# Find the largest and second largest distinct values.
if len(numbers) < 2:
    print("At least two numbers are required.")
else:
    largest = None
    second = None

    for value in numbers:
        if largest is None or value > largest:
            if largest is not None and value != largest:
                second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value

    if second is None:
        print("No second largest distinct number exists.")
    else:
        print("Second largest number:", second)
