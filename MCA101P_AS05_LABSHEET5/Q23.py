"""Q23: Swap two tuples"""
a = tuple(input('Tuple A: ').split())
b = tuple(input('Tuple B: ').split())
a, b = b, a
print('A:', a, 'B:', b)
