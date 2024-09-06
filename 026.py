s = input('слово: ')
GLAS = 'AEYUOI'
if s[0].upper() in GLAS:
    print(f'{s}way')
else:
    print(f'{s[1:]}{s[0]}ay')
