"""Q17: Remove blank lines"""
try:
    with open('sample.txt', encoding='utf-8') as f: lines=f.readlines()
    with open('sample.txt', 'w', encoding='utf-8') as f: f.writelines(x for x in lines if x.strip())
    print('Blank lines removed.')
except FileNotFoundError: print('File not found')
