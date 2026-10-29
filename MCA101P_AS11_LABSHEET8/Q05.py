"""Q5: List all tables"""
from db_common import connect
with connect() as con: print(con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
