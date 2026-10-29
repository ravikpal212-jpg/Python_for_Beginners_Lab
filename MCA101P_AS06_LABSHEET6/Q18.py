"""Q18: Remove elements of one set from another"""
a = set(input('Main set: ').split()); b = set(input('Remove these: ').split())
a.difference_update(b)
print(a)
