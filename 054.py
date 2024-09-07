from random import randint

array = ['h', 't']
win = array[randint(0,1)]
s = input('Орёл или решка? (h/t) ')
if win == s:
    print('You win')
else:
    print('Bad luck')
print('Было выбрано ОРЁЛ') if win == 'h' else print('Было выбрано РЕШКА')