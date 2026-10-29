"""Q16: Delete student by roll number"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: cur=con.execute('DELETE FROM students WHERE roll=?',(input('Roll: '),))
print('Deleted' if cur.rowcount else 'Not found')
