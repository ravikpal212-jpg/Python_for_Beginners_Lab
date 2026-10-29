"""Q7: Check whether table exists"""
from db_common import connect
name=input('Table name: ')
with connect() as con: row=con.execute('SELECT 1 FROM sqlite_master WHERE type=? AND name=?',('table',name)).fetchone()
print('Exists' if row else 'Not found')
