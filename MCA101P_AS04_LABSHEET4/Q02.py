"""Q2: Rotate a list by n positions"""
a = input("Enter items: ").split()
n = int(input("Rotate by: "))
if a:
    n %= len(a)
    a = a[-n:] + a[:-n] if n else a
print(a)
