text = input("Enter a string: ")
vowels = 0
consonants = 0

# Count alphabetic vowels and consonants.
for ch in text:
    if ("a" <= ch.lower() <= "z"):
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
