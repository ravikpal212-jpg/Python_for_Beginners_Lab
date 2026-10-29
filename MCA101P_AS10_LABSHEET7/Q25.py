"""Q25: Append CSV record"""
import csv
with open('students.csv', 'a', newline='', encoding='utf-8') as f: csv.writer(f).writerow([input('Name: '), input('Marks: ')])
print('Record appended.')
