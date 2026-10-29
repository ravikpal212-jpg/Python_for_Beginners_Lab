"""Q15: Update marks by roll number"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: cur=con.execute('UPDATE students SET marks=? WHERE roll=?',(float(input('New marks: ')),input('Roll: ')))
print('Updated' if cur.rowcount else 'Not found')
