"""Q8: Append content to file"""
with open('sample.txt', 'a', encoding='utf-8') as f: f.write(input('Append text: ') + '\n')
print('Appended.')
