"""Q13: Sort by marks descending"""
from db_common import connect
with connect() as con:
    for row in con.execute('SELECT * FROM students ORDER BY marks DESC'): print(row)
