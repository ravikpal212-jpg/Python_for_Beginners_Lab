"""Q24: Average marks"""
from db_common import connect
with connect() as con: print('Average:',con.execute('SELECT AVG(marks) FROM students').fetchone()[0])
