"""Q14: Count records"""
from db_common import connect
with connect() as con: print('Total:',con.execute('SELECT COUNT(*) FROM students').fetchone()[0])
