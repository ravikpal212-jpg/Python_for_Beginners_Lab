"""Q3: Search student by name"""
import json
try:
    with open('students.json') as f: data=json.load(f)
    name=input('Name to search: ').lower()
    print([s for s in data if s['name'].lower()==name] or 'Not found')
except FileNotFoundError: print('Run Q01 first')
