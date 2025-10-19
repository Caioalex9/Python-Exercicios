pessoas = list()
dados = list()

menor = maior = media = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]

    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    

    parar = str(input('Deseja continuar?[S/N] ')).upper().strip()


    while parar not in 'SN':
        print('Opção invalida !',end=' ')
        parar = str(input('Deseja continuar?[S/N] ')).upper().strip()
    
    if parar in 'N':
        break




print('-='*30)

print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi de {maior}kg, Peso de ,', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg, Peso de,', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

