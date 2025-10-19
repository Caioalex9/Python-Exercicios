from random import randint

numeros = (randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print()
print('-='*30)
print(f'\nO maior valor sorteado foi {max(numeros)}')
print()
print(f'O menor valor sorteado foi {min(numeros)}')
print('-='*30)