"""Q30: Combine multiple CSV files"""
import csv, glob
files=glob.glob('*.csv'); rows=[]
for file in files:
    if file != 'combined.csv':
        with open(file, newline='', encoding='utf-8') as f:
            data=list(csv.reader(f)); rows.extend(data if not rows else data[1:])
with open('combined.csv', 'w', newline='', encoding='utf-8') as f: csv.writer(f).writerows(rows)
print('Combined', len(files), 'CSV files into combined.csv')
