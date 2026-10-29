"""Q3: Remove all negative numbers"""
nums = list(map(int, input("Enter numbers: ").split()))
print([x for x in nums if x >= 0])
