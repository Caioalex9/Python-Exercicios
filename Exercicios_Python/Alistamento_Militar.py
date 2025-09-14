from datetime import date

atual = date.today().year
sexo = str(input('Sexo [M/F]: ')).upper()


if sexo == 'F':
    print('Mulheres não precisam se alistar.')
    exit()
    
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda Faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
