"""Q25: Difference between tuples"""
a = tuple(input('Tuple A: ').split())
b = tuple(input('Tuple B: ').split())
print(tuple(x for x in a if x not in b))
