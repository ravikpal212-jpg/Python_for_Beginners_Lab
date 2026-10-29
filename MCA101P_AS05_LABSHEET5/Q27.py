"""Q27: Unzip list of tuples"""
pairs = [('A', 10), ('B', 20), ('C', 30)]
names, marks = zip(*pairs)
print(list(names), list(marks))
