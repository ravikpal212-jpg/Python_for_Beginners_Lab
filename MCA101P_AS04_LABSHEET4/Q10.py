"""Q10: Convert list to string without join"""
a = input("Enter items: ").split()
result = ""
for x in a: result += x
print(result)
