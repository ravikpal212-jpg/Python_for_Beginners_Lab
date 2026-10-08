numbers = input("Enter list elements separated by spaces: ").split()

if len(numbers) == 0:
    print("The list is empty.")
else:
    values = []
    for item in numbers:
        values.append(int(item))

    largest = values[0]
    smallest = values[0]

    # Find largest and smallest using a loop.
    for value in values:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value

    print("Largest element:", largest)
    print("Smallest element:", smallest)
