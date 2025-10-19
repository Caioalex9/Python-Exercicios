listacompleta = []
listapares = []
listaimpares = []

while True:
    valor = (int(input('Digite um valor: ')))
    listacompleta.append(valor)

    parar = str(input('Deseja continuar?[S/N] ')).upper().strip()


    while parar not in 'SN':
        print('Opção invalida !', end=' ')
        parar = str(input('Deseja continuar?[S/N] ')).upper().strip()

    if valor %2 == 0:
        listapares.append(valor)
    else:
        listaimpares.append(valor)


    if parar in 'N':
        break
    
    

print('-='*30)

print(f'Lista completa: {listacompleta}')
print(f'Lista valores Pares: {listapares}')
print(f'Lista valores Impares: {listaimpares}')


print('-='*30)
