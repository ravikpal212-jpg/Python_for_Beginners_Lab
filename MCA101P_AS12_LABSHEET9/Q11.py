"""Q11: Connect to database and create students table"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: con.execute('CREATE TABLE IF NOT EXISTS students(roll TEXT PRIMARY KEY,name TEXT,age INTEGER,marks REAL)')
print('Table ready')
