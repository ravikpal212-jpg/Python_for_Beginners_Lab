text = input("Enter a string: ")
result = ""
punctuation = ".,!?;:'" + chr(34) + "()-[]{}_/\\@#$%^&*"

# Keep characters that are not punctuation.
for ch in text:
    if ch not in punctuation:
        result += ch

print("Without punctuation:", result)
