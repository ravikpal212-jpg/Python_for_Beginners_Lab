"""Q25: Group students by age"""
from db_common import connect
with connect() as con:
    for r in con.execute('SELECT age,COUNT(*) FROM students GROUP BY age'): print(r)
