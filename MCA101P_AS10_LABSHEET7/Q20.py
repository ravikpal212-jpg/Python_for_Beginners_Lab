"""Q20: Merge two text files"""
try:
    with open('file1.txt', encoding='utf-8') as a, open('file2.txt', encoding='utf-8') as b: text=a.read()+'\n'+b.read()
    with open('merged.txt', 'w', encoding='utf-8') as out: out.write(text)
    print('Saved merged.txt')
except FileNotFoundError: print('Create file1.txt and file2.txt first')
