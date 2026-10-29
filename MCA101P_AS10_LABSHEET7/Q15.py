"""Q15: Replace word in file"""
old=input('Old word: '); new=input('New word: ')
try:
    with open('sample.txt', encoding='utf-8') as f: text=f.read()
    with open('sample.txt', 'w', encoding='utf-8') as f: f.write(text.replace(old, new))
    print('Replaced.')
except FileNotFoundError: print('File not found')
