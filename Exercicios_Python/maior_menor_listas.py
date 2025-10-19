listanum = []
mai = men = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor para posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]


print('-='*30)

print(f'Você digitou os valores: {listanum}')

print(f'O MAIOR valor digitado foi {mai} na posição', end=' ')

for contador, valor in enumerate(listanum):
    if valor == mai:
        print(f'{contador}...', end=' ')
print()

print(f'O MENOR valor digitado foi {men} na posição ', end='')

for contador , valor in enumerate(listanum):
    if valor == men:
        print(f'{contador}...', end='')
print()