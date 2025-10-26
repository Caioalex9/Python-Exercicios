from time import sleep
numeros = []

def maior(* num):
    maior = cont = 0
    print('\nAnalisando os valores....')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        
    print(f'Foram analisados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

    



        
    

maior(2,4,6,9)

maior(5,6,7,8)

maior()