"""Q20: Cartesian product"""
a = set(input('Set A: ').split()); b = set(input('Set B: ').split())
print({(x, y) for x in a for y in b})
