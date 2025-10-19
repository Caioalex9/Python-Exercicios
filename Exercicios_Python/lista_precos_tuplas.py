print('-'*30)
print('{:^30}'.format('LISTA DE COMPRAS'))
print('-'*30)

lista = ('Lapis', 1.75, 
         'Borracha', 2, 
         'Caderno', 15.90, 
         'Estojo', 25.00, 
         'Transferidor', 4.20, 
         'Compasso', 9, 
         'Mochila', 120.32, 
         'Canetas', 22.30, 
         'Livro', 34.90)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')

print('-'*30)