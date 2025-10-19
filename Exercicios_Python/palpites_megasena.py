from random import randint
from time import sleep

print('-='*30)
print('{:^60}'.format('JOGA NA MEGA SENA'))
print('-='*30)

pergunta = int(input('Quantos jogos deseja gerar? '))

sorteados = list()

for j in range(0, pergunta):
    for n in range(6):
        numero = randint(1, 60)
        if numero not in sorteados:
            sorteados.append(numero)
        else:
            numero = randint(1, 60)

    sorteados.sort()

    print(f'{j+1}º jogo foi sorteado, números {sorteados} ')
    sleep(2)
    sorteados.clear()

