"""Q22: Flatten nested tuple"""
t = ((1, 2), (3, 4), (5,))
print(tuple(x for part in t for x in part))
