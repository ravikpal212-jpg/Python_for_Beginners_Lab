"""Q3: Read file line by line"""
try:
    with open('sample.txt', encoding='utf-8') as f:
        for line in f: print(line.rstrip())
except FileNotFoundError: print('sample.txt not found')
