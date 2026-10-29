"""Q11: Search for word in file"""
word=input('Search word: ').lower()
try:
    with open('sample.txt', encoding='utf-8') as f: print('Found' if word in f.read().lower().split() else 'Not found')
except FileNotFoundError: print('File not found')
