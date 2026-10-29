"""Q14: Search student by roll number"""
import sqlite3
with sqlite3.connect('crud_students.db') as con:
    row=con.execute('SELECT * FROM students WHERE roll=?',(input('Roll: '),)).fetchone()
    print(row or 'Not found')
