"""Q29: Search student by name in CSV"""
import csv
name=input('Student name: ').lower()
try:
    with open('students.csv', newline='', encoding='utf-8') as f: rows=[r for r in csv.DictReader(f) if r.get('Name','').lower()==name]
    print(rows if rows else 'No match')
except FileNotFoundError: print('CSV not found')
