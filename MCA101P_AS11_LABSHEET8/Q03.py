"""Q3: Create students table"""
from db_common import connect
with connect() as con: con.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks REAL)')
print('students table ready')
