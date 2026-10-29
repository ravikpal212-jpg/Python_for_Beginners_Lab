"""Q22: INNER JOIN students and courses"""
from db_common import connect
with connect() as con:
    for r in con.execute('SELECT students.name,courses.course FROM students INNER JOIN courses ON students.id=courses.student_id'): print(r)
