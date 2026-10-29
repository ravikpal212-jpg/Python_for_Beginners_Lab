"""Q20: Length of longest word"""
t = tuple(input('Enter words: ').split())
print(max((len(w) for w in t), default=0))
