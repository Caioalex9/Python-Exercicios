num = 0

while True:
    num = float(input('Digite um número para tabuada(NEGATIVO para PARAR): '))
    print('-'*20)
    if num < 0:
        print('Programa da tabuada encerrado. Volte sempre !')
        break
    for c in range(1, 11):
        print(f'{num:.0f} x {c:.0f} = {num*c:.0f}')
    print('-'*20)

print('-'*20)
