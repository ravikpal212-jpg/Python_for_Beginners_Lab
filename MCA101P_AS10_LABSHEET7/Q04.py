"""Q4: Count words in file"""
try:
    with open('sample.txt', encoding='utf-8') as f: print('Words:', len(f.read().split()))
except FileNotFoundError: print('File not found')
