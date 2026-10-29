"""Q30: Element-wise sum of tuples"""
a = tuple(map(int, input('Tuple A numbers: ').split()))
b = tuple(map(int, input('Tuple B numbers: ').split()))
if len(a) == len(b): print(tuple(x+y for x, y in zip(a, b)))
else: print('Tuples must have equal lengths')
