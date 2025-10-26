aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]} '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
    print('Situação é igual APROVADO!')

elif 5 <= aluno['Media'] < 7:
   aluno['Situação'] = 'Recuperação'

else:
    aluno['Situação'] = 'Reprovado'
    

print('-='*30)

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')