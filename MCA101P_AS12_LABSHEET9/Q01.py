"""Q1: Create list of student records"""
students=[]
for _ in range(int(input('Number of students: '))):
    students.append({'roll':input('Roll: '),'name':input('Name: '),'marks':float(input('Marks: '))})
print(students)
with open('students.json','w') as f: import json; json.dump(students,f,indent=2)
