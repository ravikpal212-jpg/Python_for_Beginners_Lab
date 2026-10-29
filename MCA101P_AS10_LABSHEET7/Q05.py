"""Q5: Count lines and characters"""
try:
    with open('sample.txt', encoding='utf-8') as f: s=f.read()
    print('Lines:', len(s.splitlines()), 'Characters:', len(s))
except FileNotFoundError: print('File not found')
