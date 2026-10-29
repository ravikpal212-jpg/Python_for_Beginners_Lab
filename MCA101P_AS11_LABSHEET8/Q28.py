"""Q28: Handle database errors"""
import sqlite3
from db_common import connect
try:
    with connect() as con: con.execute('INSERT INTO missing_table VALUES(1)')
except sqlite3.Error as e: print('Database error:',e)
