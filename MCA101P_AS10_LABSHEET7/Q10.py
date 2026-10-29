"""Q10: Convert file content to uppercase"""
try:
    with open('sample.txt', encoding='utf-8') as f: text=f.read()
    print(text.upper())
except FileNotFoundError: print('File not found')
