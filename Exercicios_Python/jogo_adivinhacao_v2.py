from random import randint

computador = randint(0, 10)

print('Sou seu computador. Estou pensando em um número de 0 a 10')
print('Será que você consegue adivinhar? ')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
            acertou = True
    else:
        if jogador < computador:
             print('Mais... tente novamente')
        if jogador > computador:
             print('Menos...Tente novamente')

print('Você acertou em {} tentativas '.format(palpites))
