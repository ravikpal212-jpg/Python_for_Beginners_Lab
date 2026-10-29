"""Q12: Find maximum and minimum marks without max/min"""
marks = {"Asha": 82, "Ravi": 91, "Neha": 76}
hi = lo = next(iter(marks.values()))
for x in marks.values():
    if x > hi: hi = x
    if x < lo: lo = x
print("Maximum:", hi, "Minimum:", lo)
