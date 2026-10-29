"""Q7: Check whether list is sorted"""
a = list(map(int, input("Enter numbers: ").split()))
print("Sorted" if all(a[i] <= a[i+1] for i in range(len(a)-1)) else "Not sorted")
