"""Q8: Insert one student"""
from db_common import connect
with connect() as con: con.execute('INSERT INTO students(name,age,marks) VALUES(?,?,?)',(input('Name: '),int(input('Age: ')),float(input('Marks: '))))
print('Inserted')
