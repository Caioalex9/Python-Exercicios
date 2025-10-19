listanumero = []

while True:
    listanumero.append(int(input('Digite um numero: ')))

    parar = str(input('Deseja continuar?[S/N] ')).upper()

    while parar not in 'SN':
        print('Opção invalida !', end=' ')
        parar = str(input('Deseja continuar?[S/N] ')).upper()

    if parar in 'N':
        print('Fim do programa')
        break

print('-='*30)

print(f'Os números digitados foram: {listanumero}')
print(f'Ao total foram digitados {len(listanumero)} números')
listanumero.sort()
print(f'Os números apresentados em ordem decrescente {listanumero[::-1]}')

if 5 in listanumero:
    print(f'O valor 5 foi digitado {listanumero.count(5)}ª vezes')
else:
    print('O valor 5 não foi encontrado na lista')

print('-='*30)