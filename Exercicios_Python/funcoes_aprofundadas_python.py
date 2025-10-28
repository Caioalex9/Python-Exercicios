def leiaInt(msg):
    while True:

        try:
            n = int(input(msg))

        # except Exception as erro:
        #     print(f'\033[0;31mERRO ! Digite um número inteiro.{erro.__class__}.\033[m')
        

        except(ValueError, TypeError):
            print('\033[0;31mERRO ! Digite apenas valores INTEIROS\033[m')
            continue

        except(KeyboardInterrupt):
            print(f'\n\033[0;31mERRO ! O usuario prefiriu não digitar um numero INTEIRO!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):

    while True:
        try:
            r = float(input(msg))
        
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO ! Digite um numero REAL valido !\033[m')
            continue

        except(KeyboardInterrupt):
            print(f'\n\033[0;31mERRO ! O usuario prefiriu não digitar o numero REAL!\033[m')
            return 0
        
        else:
            return r


num = leiaInt(f'\033[0;33mDigite um Inteiro: \033[m')
real = leiaFloat(f'\033[0;34mDigite um Real: \033[m')

print(f'\033[0;32mO valor Inteiro digitado foi {num}, e o real foi {real}\033[m')