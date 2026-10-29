"""Q20: Empty table while keeping structure"""
from db_common import connect
with connect() as con: con.execute('DELETE FROM students')
print('Table emptied; structure kept')
