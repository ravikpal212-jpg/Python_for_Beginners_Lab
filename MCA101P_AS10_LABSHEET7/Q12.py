"""Q12: Count specific word"""
word=input('Word: ').lower()
try:
    with open('sample.txt', encoding='utf-8') as f: print('Count:', f.read().lower().split().count(word))
except FileNotFoundError: print('File not found')
