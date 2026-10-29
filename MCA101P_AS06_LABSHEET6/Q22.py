"""Q22: Find duplicates using set"""
a = input('Enter items: ').split(); seen = set(); dup = set()
for x in a:
    if x in seen: dup.add(x)
    seen.add(x)
print(dup)
