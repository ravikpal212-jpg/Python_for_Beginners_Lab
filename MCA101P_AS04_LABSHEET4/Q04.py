"""Q4: Product of list elements"""
nums = list(map(int, input("Enter numbers: ").split()))
product = 1
for x in nums: product *= x
print("Product:", product)
