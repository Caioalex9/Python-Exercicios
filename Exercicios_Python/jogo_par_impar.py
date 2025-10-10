from random import randint
print('-='*20)
print('     VAMOS JOGAR PAR OU IMPAR     ') 
print('-='*20)

computador = randint(0, 11)
cont = soma = resultado = 0

while True:

    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    poi = ' '
    while poi not in 'PI':
        poi = str(input('Par ou Impar?[P/I] ')).upper().strip()[0]

    print('-='*20)
    print(f'Você jogou {jogador} e o computador {computador}. total deu {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else ' DEU IMPAR' )


    if poi == 'P':
        if soma % 2 == 0:
            print('Você Venceu !')
            cont += 1
        else:
            print('Você Perdeu !')
            break
    if poi == 'I':
        if soma % 2 == 0:
            print('Você Venceu !')
            cont += 1
        else:
            print('Você perdeu !')
            break
    print('Vamos jogar novamente...')


print('-='*20)
print(f'GAME OVER ! Você venceu {cont} vezes')
