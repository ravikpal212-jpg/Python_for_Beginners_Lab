"""Q28: Nested dictionary for student details"""
students = {}
for _ in range(2):
    roll = input("Roll: ")
    students[roll] = {"Name": input("Name: "), "Marks": float(input("Marks: "))}
print(students)
