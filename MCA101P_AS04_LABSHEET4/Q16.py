"""Q16: Sort dictionary by values"""
d = {"A": 40, "B": 20, "C": 35}
print(dict(sorted(d.items(), key=lambda x: x[1])))
