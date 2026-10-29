"""Q9: Save student data to text file and read it"""
data=input('Enter student details: ')
with open('student.txt','w',encoding='utf-8') as f: f.write(data)
with open('student.txt',encoding='utf-8') as f: print(f.read())
