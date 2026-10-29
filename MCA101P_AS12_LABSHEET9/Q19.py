"""Q19: Find student with highest marks"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: print(con.execute('SELECT * FROM students ORDER BY marks DESC LIMIT 1').fetchone() or 'No records')
