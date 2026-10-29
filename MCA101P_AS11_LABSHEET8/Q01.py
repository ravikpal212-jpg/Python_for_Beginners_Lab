"""Q1: Connect to database and show success"""
import sqlite3
con=sqlite3.connect('student_db.sqlite')
print('Connected successfully')
con.close()
