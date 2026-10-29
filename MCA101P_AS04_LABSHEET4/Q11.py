"""Q11: Create and display student marks dictionary"""
n = int(input("Number of students: "))
marks = {}
for _ in range(n):
    name = input("Name: ")
    marks[name] = float(input("Marks: "))
print(marks)
