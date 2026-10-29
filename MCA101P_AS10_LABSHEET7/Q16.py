"""Q16: Display first and last lines"""
try:
    with open('sample.txt', encoding='utf-8') as f: lines=f.readlines()
    print('First:', lines[0].rstrip() if lines else 'Empty', '\nLast:', lines[-1].rstrip() if lines else 'Empty')
except FileNotFoundError: print('File not found')
