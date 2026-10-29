"""Q14: Display longest line"""
try:
    with open('sample.txt', encoding='utf-8') as f: lines=f.readlines()
    print(max(lines, key=len).rstrip() if lines else 'Empty file')
except FileNotFoundError: print('File not found')
