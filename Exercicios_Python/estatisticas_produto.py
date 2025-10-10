print('-'*40)
print('      LOJA SUPER BARATÃO DO CAIÃO      ')
print('-'*40)

totc = totm = produtobarato = itembarato = cont = 0
barato = ''
while True:

    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    totc += preco
    cont += 1

    if preco > 1000:
        totm += 1

    if cont == 1 or preco < produtobarato:
        produtobarato = preco
        barato = nome

    resp = ' ' 

    while resp not in 'SN':
        resp = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break

print('-'*40)
print(f'O total da compra foi de R${totc}')
print(f'Temos {totm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${produtobarato}')
print('FIM DO PROGRAMA')
