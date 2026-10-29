"""Q17: Update student name"""
from db_common import connect
with connect() as con: cur=con.execute('UPDATE students SET name=? WHERE id=?',(input('New name: '),int(input('Student ID: '))))
print('Updated' if cur.rowcount else 'ID not found')
