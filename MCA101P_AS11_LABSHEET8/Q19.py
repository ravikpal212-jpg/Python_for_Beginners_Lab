"""Q19: Delete students with marks below 40"""
from db_common import connect
with connect() as con: cur=con.execute('DELETE FROM students WHERE marks<40')
print('Deleted:',cur.rowcount)
