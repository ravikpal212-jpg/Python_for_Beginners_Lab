"""Q23: Average of numeric CSV column"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as f: rows=list(csv.DictReader(f))
    vals=[float(r['Marks']) for r in rows if r.get('Marks')]
    print('Average marks:', sum(vals)/len(vals) if vals else 0)
except (FileNotFoundError, KeyError, ValueError) as e: print('Check CSV/Marks column:', e)
