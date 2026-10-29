"""Q2: Read entire text file"""
try:
    with open('sample.txt', encoding='utf-8') as f: print(f.read())
except FileNotFoundError: print('sample.txt not found')
