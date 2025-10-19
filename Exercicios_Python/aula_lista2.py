# galera = [['Maria', 25],['João', 46],['Caio', 28], ['Pit', 25], ['Davi', 44]]

# for pessoa in galera:
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

galera = list()
dados = list()
totmai = totmen = 0

for contador in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #dados[:] para fazer uma copia, caso não haja vai fazer ligação e ambas serão alteradas
    dados.clear()

for pessoa in galera:
    if pessoa[1] > 21:
        print(f'{pessoa[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totmen += 1

print(f'Ao total temos {totmai} pessoas maior de idade e {totmen} menor de idade')