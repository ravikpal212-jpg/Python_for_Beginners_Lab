"""Q29: Functions to insert and fetch data"""
from db_common import connect
def add(name,age,marks):
    with connect() as con: con.execute('INSERT INTO students(name,age,marks) VALUES(?,?,?)',(name,age,marks))
def fetch():
    with connect() as con: return con.execute('SELECT * FROM students').fetchall()
add(input('Name: '),int(input('Age: ')),float(input('Marks: ')))
print(fetch())
