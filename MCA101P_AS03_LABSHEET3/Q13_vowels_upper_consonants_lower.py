text = input("Enter a string: ")
result = ""

# Convert vowels to uppercase and consonants to lowercase.
for ch in text:
    lower_ch = ch.lower()
    if lower_ch in "aeiou":
        result += lower_ch.upper()
    elif "a" <= lower_ch <= "z":
        result += lower_ch
    else:
        result += ch

print("Result:", result)
