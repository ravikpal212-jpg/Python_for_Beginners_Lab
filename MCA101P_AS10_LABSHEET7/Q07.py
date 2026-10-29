"""Q7: Write multiple user lines"""
with open('sample.txt', 'w', encoding='utf-8') as f:
    while (line := input('Line (blank to stop): ')):
        f.write(line + '\n')
print('Saved.')
