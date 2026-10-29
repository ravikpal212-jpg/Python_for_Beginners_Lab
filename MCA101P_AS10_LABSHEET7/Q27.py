"""Q27: Display selected Name and Marks columns"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f): print(row.get('Name',''), row.get('Marks',''))
except FileNotFoundError: print('CSV not found')
