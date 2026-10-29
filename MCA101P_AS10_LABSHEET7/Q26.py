"""Q26: Copy CSV file"""
import csv
try:
    with open('students.csv', newline='', encoding='utf-8') as src: rows=list(csv.reader(src))
    with open('students_copy.csv', 'w', newline='', encoding='utf-8') as dst: csv.writer(dst).writerows(rows)
    print('Copied to students_copy.csv')
except FileNotFoundError: print('CSV not found')
