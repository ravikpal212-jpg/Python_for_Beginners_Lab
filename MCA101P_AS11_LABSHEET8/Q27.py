"""Q27: Import CSV into students"""
import csv
from db_common import connect
with open('students_import.csv',newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
with connect() as con: con.executemany('INSERT INTO students(name,age,marks) VALUES(?,?,?)',[(r['name'],int(r['age']),float(r['marks'])) for r in rows])
print('Imported',len(rows))
