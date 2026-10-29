"""Q9: Insert multiple students"""
from db_common import connect
rows=[]
for _ in range(int(input('How many? '))): rows.append((input('Name: '),int(input('Age: ')),float(input('Marks: '))))
with connect() as con: con.executemany('INSERT INTO students(name,age,marks) VALUES(?,?,?)',rows)
print('Inserted',len(rows),'records')
