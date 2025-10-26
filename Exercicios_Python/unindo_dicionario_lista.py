pessoa = {}
galera = []

totidade = totmulher = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o nome: '))

    pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper().strip()

    while pessoa['Sexo'] not in 'MF':
        print('Opção invalida !', end=' ')
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper().strip()

    pessoa['Idade'] = int(input('Idade: '))

    totidade += pessoa['Idade']

    galera.append(pessoa.copy())

    resp = str(input('Deseja continuar?[S/N] ')).upper().strip()

    while resp not in 'SN':
        print('Opção invalida !', end=' ')
        resp = str(input('Deseja continuar?[S/N] ')).upper().strip()

    if resp in 'N':
        break

print('-='*30)

print(f'Pessoas cadastradas: {galera}')

print('-='*30)

print(f'Ao total foram cadastradas {len(galera)} pessoas')

media = totidade / len(galera)
print(f'A media de idade foi: {media:5.2f} anos')

print(f'As mulheres cadastradas foram: ', end=' ')

for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}', end=' ,')
print()

print('Lista das pessoas acimas da media')

for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v} ;', end=' ')
        print()

print(' <<< ENCERRANDO >>> ')