"""Q28: Find repeated items"""
t = tuple(input('Enter items: ').split())
print(tuple(x for x in dict.fromkeys(t) if t.count(x) > 1))
