"""Q22: Read CSV file"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as f:
        for row in csv.reader(f): print(row)
except FileNotFoundError: print('students.csv not found')
