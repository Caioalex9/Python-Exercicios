from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

ranking = list()

print('Valores Sorteados')
for k, v in jogo.items():
    print(f' O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)


print(ranking) 

print('-='*30)
print(' == RANKING DOS JOGADORES == ')

for i, v in enumerate(ranking):
    print(f'  O {i+1}º lugar: {v[0]} com {v[1]} .')
    sleep(1)

    
