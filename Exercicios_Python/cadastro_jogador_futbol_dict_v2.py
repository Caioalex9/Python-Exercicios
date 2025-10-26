jogador = {}
partidas = []
time = []

while True:

    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas jogadas: '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'Quantidade de gols do campeonato, {c+1}º jogo: ')))

    jogador['Gols'] = partidas[:]

    jogador['Total'] = sum(partidas)

    time.append(jogador.copy())

    resp = str(input('Deseja continuar?[S/N] ')).upper().strip()
    while resp not in 'SN':
        print('Opção invalida !', end=' ')
        resp = str(input('Deseja continuar?[S/N] ')).upper().strip()

    if resp == 'N':
        break

print('-='*30)

print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)

for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para PARAR) '))

    if busca == 999:
        break

    if busca >= len(time):
        print(f'Não existe jogador com codigo da {busca}')
    
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'  No jogo {i+1} fez {g} gols')

    print('-'*40)

print(' << VOLTE SEMPRE >> ')