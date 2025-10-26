from random import randint
from time import sleep
numeros = []


def sorteio ():
    print('Os 5 números sorteados foram: ', end=' ')
    for v in range(0, 5):
        sorteio = randint(1, 10)
        numeros.append(sorteio)
        
        print(f'{sorteio}', flush=True, end=' ')
        sleep(0.3)

    print('Pronto')


def somaPar():
    pares = 0
    print ()
    print('A soma dos valores: ', end=' ')
    for valor in numeros:
        if valor % 2 == 0:
            pares += valor
            print(f'{valor},', end=' ')
        
    print(f'É {pares}')

    


sorteio()
somaPar()