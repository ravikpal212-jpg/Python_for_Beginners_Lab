"""Q18: Sort records by student name"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: print(con.execute('SELECT * FROM students ORDER BY name').fetchall())
