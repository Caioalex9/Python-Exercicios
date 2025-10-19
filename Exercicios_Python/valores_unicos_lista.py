listanumero = []


while True:

    numero = int(input('Digite um valor: '))

    if numero not in listanumero:
        listanumero.append(numero)
        print('Valor adicionado com sucesso...')

    else:
        print('Voce ja digitou valor !', end=' ')


    parar = str(input('Deseja continuar[S/N]? ')).strip().upper()
    
    while parar not in 'SN':
        print('Valor invalido !', end=' ')
        parar = str(input('Deseja continuar[S/N]? ')).strip().upper()

    if parar == 'N':
        break

listanumero.sort()

print('-='*30)

print(f'Você digitou os valores: {listanumero}')