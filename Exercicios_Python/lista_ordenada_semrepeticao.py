listanumero = []


for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or c > listanumero[-1]:
        listanumero.append(numero)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(listanumero):
            if numero <= listanumero[pos]:
                listanumero.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1      


print(f'Os valores digitados em ordem foram {listanumero}')
