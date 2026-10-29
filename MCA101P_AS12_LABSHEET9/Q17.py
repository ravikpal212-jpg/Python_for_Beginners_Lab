"""Q17: Count database records"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: print('Total:',con.execute('SELECT COUNT(*) FROM students').fetchone()[0])
