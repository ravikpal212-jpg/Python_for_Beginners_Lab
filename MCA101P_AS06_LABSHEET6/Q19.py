"""Q19: Power set"""
from itertools import chain, combinations
s = set(input('Enter items: ').split())
items = list(s)
print([set(c) for r in range(len(items)+1) for c in combinations(items, r)])
