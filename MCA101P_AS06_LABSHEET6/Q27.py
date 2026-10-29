"""Q27: Check anagram using sets"""
a = input('First word: ').lower().replace(' ', ''); b = input('Second word: ').lower().replace(' ', '')
print(len(a) == len(b) and set(a) == set(b))
