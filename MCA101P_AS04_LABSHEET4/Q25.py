"""Q25: Word frequency in paragraph"""
import re
words = re.findall(r"\b\w+\b", input("Paragraph: ").lower())
freq = {}
for w in words: freq[w] = freq.get(w, 0) + 1
print(freq)
