"""Q18: Remove a key from dictionary"""
d = {"a": 1, "b": 2, "c": 3}
key = input("Key to remove: ")
d.pop(key, None)
print(d)
