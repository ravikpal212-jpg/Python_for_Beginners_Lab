"""Q8: Find index of an element"""
t = tuple(input('Enter items: ').split())
x = input('Element: ')
print(t.index(x) if x in t else 'Not found')
