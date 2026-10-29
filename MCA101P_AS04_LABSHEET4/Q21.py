"""Q21: Find key with maximum value"""
d = {"A": 45, "B": 88, "C": 71}
print(max(d, key=d.get))
