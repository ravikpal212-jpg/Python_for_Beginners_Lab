"""Q13: Character frequency dictionary"""
s = input("Enter text: ")
freq = {}
for ch in s: freq[ch] = freq.get(ch, 0) + 1
print(freq)
