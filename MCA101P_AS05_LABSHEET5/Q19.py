"""Q19: Remove duplicate elements"""
t = tuple(input('Enter items: ').split())
print(tuple(dict.fromkeys(t)))
