"""Q30: All basic set operations"""
a = set(input('Set A: ').split()); b = set(input('Set B: ').split())
print('Union:', a|b, '\nIntersection:', a&b, '\nDifference:', a-b, '\nSymmetric difference:', a^b)
