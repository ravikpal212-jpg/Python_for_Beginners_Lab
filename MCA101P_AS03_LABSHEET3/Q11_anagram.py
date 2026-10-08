first = input("Enter the first string: ")
second = input("Enter the second string: ")

# Compare character frequencies after ignoring spaces and case.
frequency = {}
for ch in first.lower():
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

for ch in second.lower():
    if ch != " ":
        if ch in frequency:
            frequency[ch] -= 1
        else:
            frequency[ch] = -1

is_anagram = True
for ch in frequency:
    if frequency[ch] != 0:
        is_anagram = False
        break

if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
