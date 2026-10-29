"""Q24: Count CSV rows and columns"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as f: rows=list(csv.reader(f))
    print('Data rows:', max(0, len(rows)-1), 'Columns:', len(rows[0]) if rows else 0)
except FileNotFoundError: print('CSV not found')
