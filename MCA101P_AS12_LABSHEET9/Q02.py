"""Q2: Read and display student records"""
import json
try:
    with open('students.json') as f: students=json.load(f)
    for s in students: print(s)
except FileNotFoundError: print('Run Q01 first')
