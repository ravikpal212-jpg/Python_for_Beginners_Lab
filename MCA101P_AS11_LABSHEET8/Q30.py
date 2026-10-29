"""Q30: Menu-driven student management"""
from db_common import connect
while True:
    print('1 Add  2 View  3 Update  4 Delete  0 Exit')
    ch=input('Choice: ')
    if ch=='1':
        with connect() as con: con.execute('INSERT INTO students(name,age,marks) VALUES(?,?,?)',(input('Name: '),int(input('Age: ')),float(input('Marks: '))))
    elif ch=='2':
        with connect() as con: print(con.execute('SELECT * FROM students').fetchall())
    elif ch=='3':
        with connect() as con: con.execute('UPDATE students SET marks=? WHERE id=?',(float(input('Marks: ')),int(input('ID: '))))
    elif ch=='4':
        with connect() as con: con.execute('DELETE FROM students WHERE id=?',(int(input('ID: ')),))
    elif ch=='0': break
    else: print('Invalid choice')
