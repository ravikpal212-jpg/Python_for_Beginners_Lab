"""Q26: Export students to CSV"""
import csv
from db_common import connect
with connect() as con: rows=con.execute('SELECT * FROM students').fetchall()
with open('students_export.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['id','name','age','marks']); w.writerows(rows)
print('Exported')
