"""Q28: Find highest marks in CSV"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as f: rows=list(csv.DictReader(f))
    best=max(rows, key=lambda r: float(r['Marks'])) if rows else None
    print(best if best else 'No records')
except (FileNotFoundError, KeyError, ValueError) as e: print('Check CSV:', e)
