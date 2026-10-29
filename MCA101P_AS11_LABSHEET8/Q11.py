"""Q11: Display name and marks only"""
from db_common import connect
with connect() as con:
    for row in con.execute('SELECT name,marks FROM students'): print(row)
