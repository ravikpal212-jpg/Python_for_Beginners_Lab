"""Q6: Display even-numbered lines"""
try:
    with open('sample.txt', encoding='utf-8') as f:
        for n, line in enumerate(f, 1):
            if n % 2 == 0: print(line.rstrip())
except FileNotFoundError: print('File not found')
