"""Q22: Dictionary of numbers and squares"""
n = int(input("n: "))
print({x: x*x for x in range(1, n+1)})
