"""Q10: Display all student records"""
from db_common import connect
with connect() as con:
    for row in con.execute('SELECT * FROM students'): print(row)
