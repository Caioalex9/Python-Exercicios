def leiaint(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            ok = True
            print(f'voce digitou {valor}')
            
        else:
            print('\033[0;031mDigite valor valido\033[m')#pintar vermelho \033[0;031m \033[m

        if ok:
            break
    return valor



n = leiaint('Digite um numero: ')

