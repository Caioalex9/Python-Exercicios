from datetime import datetime
from time import sleep

trabalhador = dict()



trabalhador['Nome'] = str(input('Nome do trabalhador: '))

nasc = int(input('Qual ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - nasc


trabalhador['CTPS'] = int(input('Número da carteira de trabalho(0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salario atual R$ '))
    trabalhador['Aposentar'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)

print('-='*30)

for k, v in trabalhador.items():
    print(f'  - {k} e igual a {v}')
    sleep(1)


print(trabalhador)