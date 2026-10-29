"""Q4: Describe students table"""
from db_common import connect
with connect() as con: print(con.execute('PRAGMA table_info(students)').fetchall())
