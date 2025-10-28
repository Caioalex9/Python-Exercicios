from time import sleep

def menu(msg):
    print('-'*30)
    print(f'{'Menu principal':^30}')
    print('-'*30)

    print(f'\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas.\033[m')
    print(f'\033[0;33m2\033[m - \033[0;34mCadastrar novas pessoas.\033[m')
    print(f'\033[0;33m3\033[m - \033[0;34mSair do sistema.\033[m')

    print('-'*30)

    while True:
        try:
            opcao = int(input(f'\033[0;33m{msg}\033[m'))

        except(ValueError, TypeError):
            sleep(0.5)
            print(f'\033[0;31mERRO: Por favor digite um número inteiro valido !\033[m')
            continue

        else:
        
            if opcao == 1:
                sleep(1)
                registro()
                

            elif opcao == 2:
                sleep(1)
                cadastrar()

            elif opcao == 3:
                sleep(1)
                encerrando()
                break
            
            else:
                sleep(0.5)
                print(f'\033[0;31mERRO ! Digite uma opção valida !\033[m')






def registro():
    print('-'*30)
    print(f'{'OPÇÃO 1':^30}')
    print('-'*30)





def cadastrar():
    print('-'*30)
    print(f'{'OPÇÃO 2':^30}')
    print('-'*30)

def encerrando():
    print('-'*30)
    print(f'{'ENCERRANDO PROGRAMA ... ATE LOGO !'}')
    print('-'*30)