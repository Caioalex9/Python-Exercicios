maiordz = men = menormu =  0
print('-'*40)
print('      ANÁLISE DE DADOS DO GRUPO     ')
print('-'*40)

while True:
    idade = int(input('Idade: '))

    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]

    while sexo not in 'MF':
        print('SEXO INVALIDO. Tente novamente !')
    
    if idade >= 18:
        maiordz += 1

    if sexo in 'M':
        men += 1

    elif sexo in 'F' and idade < 20:
        menormu += 1

    continuar = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        print('INFORMAÇÃO INVALIDA ! Tente novamente')
        continuar = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]

    if continuar in 'N':
        break

print('-'*40)
print(f'Total de pessoas com mais de 18 anos foram {maiordz}')
print(f'Ao todo temos {men} homens cadastrados')
print(f'Temos {menormu} mulheres com menos de 20 anos')

