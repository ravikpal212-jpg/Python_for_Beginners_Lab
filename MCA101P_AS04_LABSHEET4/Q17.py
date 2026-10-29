"""Q17: Update dictionary value"""
d = {"name": "Ravi", "marks": 70}
key = input("Key to update (name/marks): ")
if key in d:
    value = input("New value: ")
    d[key] = value
print(d)
