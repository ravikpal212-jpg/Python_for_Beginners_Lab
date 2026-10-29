"""Q18: Delete student by ID"""
from db_common import connect
with connect() as con: cur=con.execute('DELETE FROM students WHERE id=?',(int(input('Student ID: ')),))
print('Deleted' if cur.rowcount else 'ID not found')
