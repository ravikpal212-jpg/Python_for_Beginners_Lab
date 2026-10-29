"""Q18: Store unique words in another file"""
try:
    with open('sample.txt', encoding='utf-8') as f: words=f.read().split()
    with open('unique_words.txt', 'w', encoding='utf-8') as f: f.write('\n'.join(dict.fromkeys(words)))
    print('Saved unique_words.txt')
except FileNotFoundError: print('File not found')
