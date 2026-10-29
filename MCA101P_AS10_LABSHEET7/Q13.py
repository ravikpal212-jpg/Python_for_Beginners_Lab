"""Q13: Sum and average of numbers in file"""
try:
    with open('numbers.txt', encoding='utf-8') as f: nums=[float(x) for x in f.read().split()]
    print('Sum:', sum(nums), 'Average:', sum(nums)/len(nums) if nums else 0)
except (FileNotFoundError, ValueError) as e: print('Check numbers.txt:', e)
