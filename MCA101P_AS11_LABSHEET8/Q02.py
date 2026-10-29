"""Q2: Create a new database"""
import sqlite3
con=sqlite3.connect('new_database.sqlite')
print('Database created')
con.close()
