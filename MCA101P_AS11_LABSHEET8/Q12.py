"""Q12: Students with marks above 80"""
from db_common import connect
with connect() as con:
    for row in con.execute('SELECT * FROM students WHERE marks>80'): print(row)
