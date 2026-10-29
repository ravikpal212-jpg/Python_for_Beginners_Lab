"""Q1: Create and write text file"""
with open('sample.txt', 'w', encoding='utf-8') as f: f.write(input('Text to write: '))
print('File written.')
