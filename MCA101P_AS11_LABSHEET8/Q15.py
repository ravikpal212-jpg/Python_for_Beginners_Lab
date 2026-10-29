"""Q15: Top three students"""
from db_common import connect
with connect() as con:
    for row in con.execute('SELECT * FROM students ORDER BY marks DESC LIMIT 3'): print(row)
