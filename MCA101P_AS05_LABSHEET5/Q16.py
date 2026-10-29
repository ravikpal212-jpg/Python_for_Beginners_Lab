"""Q16: Sort tuple of strings"""
t = tuple(input('Enter words: ').split())
print(tuple(sorted(t, key=str.lower)))
