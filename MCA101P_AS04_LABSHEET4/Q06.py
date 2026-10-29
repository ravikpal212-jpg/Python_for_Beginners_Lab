"""Q6: Split list into two halves"""
a = input("Enter items: ").split()
mid = (len(a)+1)//2
print("First:", a[:mid], "\nSecond:", a[mid:])
