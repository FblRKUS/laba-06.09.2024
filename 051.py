count = 3
while count > 0:
    print(f'There are {count} green bottles hanging on the wall, {count} green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
    a = int(input('how many green bottles will be hanging on the wall? '))
    count -= 1
    if a == count:
        print(f'There will be {count} green bottles hanging on the wall')
    else:
        print('No, try again')
print('There are no more green bottles hanging on the wall')
