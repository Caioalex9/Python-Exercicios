valores = list()
pares = list()
impares = list()

for p in range(1, 8):
    valor = int(input(f'Digite o {p}º valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort()

print('-='*30)

print(f'Os valores digitados foram: {valores}')
print(f'Os valores PARES digitados foram: {pares}')
print(f'Os valores IMPARES digitados foram: {impares}')