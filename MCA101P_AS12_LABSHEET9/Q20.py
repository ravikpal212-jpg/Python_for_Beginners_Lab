"""Q20: Menu-driven database CRUD"""
import sqlite3
DB='crud_students.db'
with sqlite3.connect(DB) as con: con.execute('CREATE TABLE IF NOT EXISTS students(roll TEXT PRIMARY KEY,name TEXT,age INTEGER,marks REAL)')
while True:
    c=input('1 Add 2 View 3 Update 4 Delete 0 Exit: ')
    with sqlite3.connect(DB) as con:
        if c=='1': con.execute('INSERT OR REPLACE INTO students VALUES(?,?,?,?)',(input('Roll: '),input('Name: '),int(input('Age: ')),float(input('Marks: '))))
        elif c=='2': print(con.execute('SELECT * FROM students').fetchall())
        elif c=='3': con.execute('UPDATE students SET marks=? WHERE roll=?',(float(input('Marks: ')),input('Roll: ')))
        elif c=='4': con.execute('DELETE FROM students WHERE roll=?',(input('Roll: '),))
        elif c=='0': break
        else: print('Invalid choice')
