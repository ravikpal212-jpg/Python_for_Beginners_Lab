import sqlite3

DB = 'student_db.sqlite'

def connect():
    con = sqlite3.connect(DB)
    con.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks REAL)')
    con.execute('CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, course TEXT, student_id INTEGER)')
    return con
