"""Q21: Create CSV file"""
import csv
with open('students.csv', 'w', newline='', encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['Name','Marks']); w.writerow([input('Name: '), input('Marks: ')])
print('Created students.csv')
