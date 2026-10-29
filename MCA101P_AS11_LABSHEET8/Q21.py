"""Q21: Create courses table and insert data"""
from db_common import connect
with connect() as con:
    con.execute('CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, course TEXT, student_id INTEGER)')
    con.execute('INSERT INTO courses(course,student_id) VALUES(?,?)',(input('Course: '),int(input('Student ID: '))))
print('Course added')
