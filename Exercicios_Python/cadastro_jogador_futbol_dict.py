jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input('Quantas partidas jogadas: '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantidade de gols do campeonato, {c+1}º jogo: ')))

jogador['Gols'] = partidas[:]

jogador['Total'] = sum(partidas)

print('-='*30)

print(jogador)
print('-='*30)

for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')

for i, v in enumerate(jogador["Gols"]):
    print(f'  => na partida {i+1}, fez {v} gols')
    
print(f'Foi total de {jogador["Total"]} gols')