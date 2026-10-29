"""Q16: Update marks by ID"""
from db_common import connect
with connect() as con: cur=con.execute('UPDATE students SET marks=? WHERE id=?',(float(input('New marks: ')),int(input('Student ID: '))))
print('Updated' if cur.rowcount else 'ID not found')
