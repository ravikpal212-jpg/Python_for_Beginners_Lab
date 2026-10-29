"""Q12: Insert student record"""
import sqlite3
with sqlite3.connect('crud_students.db') as con: con.execute('CREATE TABLE IF NOT EXISTS students(roll TEXT PRIMARY KEY,name TEXT,age INTEGER,marks REAL)'); con.execute('INSERT OR REPLACE INTO students VALUES(?,?,?,?)',(input('Roll: '),input('Name: '),int(input('Age: ')),float(input('Marks: '))))
print('Saved')
