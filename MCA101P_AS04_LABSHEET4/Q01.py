"""Q1: Find sum and average of list elements"""
nums = list(map(float, input("Enter numbers: ").split()))
total = sum(nums)
print("Sum:", total, "\nAverage:", total / len(nums) if nums else 0)
