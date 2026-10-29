"""Q19: Sort words alphabetically to new file"""
try:
    with open('sample.txt', encoding='utf-8') as f: words=f.read().split()
    with open('sorted_words.txt', 'w', encoding='utf-8') as f: f.write('\n'.join(sorted(words, key=str.lower)))
    print('Saved sorted_words.txt')
except FileNotFoundError: print('File not found')
