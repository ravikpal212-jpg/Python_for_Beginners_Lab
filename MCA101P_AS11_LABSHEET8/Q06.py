"""Q6: Drop a table"""
from db_common import connect
name=input('Table name to drop: ')
if name in ('students','courses'):
    with connect() as con: con.execute(f'DROP TABLE IF EXISTS {name}')
    print('Dropped', name)
else: print('Only students/courses allowed')
