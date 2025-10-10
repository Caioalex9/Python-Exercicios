from datetime import date

atual = date.today().year
qts_maior = 0
qts_menor = 0

for c in range(1, 8):
    ano = int(input('Digite o ano que a {}ª pessoa nascer? '.format(c)))
    idade = atual - ano

    if idade >= 18:
        qts_maior += 1
        print('Você é maior de idade,tem  {} anos'.format(idade))
    else:
        qts_menor += 1 
        print('Você é menor de idade, tem {} anos'.format(idade))
print('Ao todo tivemos {} pessoas MAIORES de idade'.format(qts_maior))
print('Ao todo tivemos {} pessoas MENORES de idade'.format(qts_menor))



