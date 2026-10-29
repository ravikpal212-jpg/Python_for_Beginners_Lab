"""Q24: Common elements between tuples"""
a = tuple(input('Tuple A: ').split())
b = tuple(input('Tuple B: ').split())
print(tuple(x for x in dict.fromkeys(a) if x in b))
