"""Q29: Check all elements same"""
t = tuple(input('Enter items: ').split())
print(bool(t) and all(x == t[0] for x in t))
