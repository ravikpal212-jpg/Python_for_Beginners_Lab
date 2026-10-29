"""Q24: Invert dictionary"""
d = {"a": 1, "b": 2, "c": 3}
print({v: k for k, v in d.items()})
