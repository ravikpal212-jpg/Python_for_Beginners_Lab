"""Q8: Find pairs with a given sum"""
a = list(map(int, input("Enter numbers: ").split()))
target = int(input("Target sum: "))
print([(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a)) if a[i]+a[j] == target])
