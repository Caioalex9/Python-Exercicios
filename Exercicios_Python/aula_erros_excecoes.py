try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'Ocorreu um erro no programa ! {erro.__class__}')

except (ValueError, TypeError): #ValueError(Esperava um valor inteiro e recebe uma string), TypeError(Erro no tipo de dado)
    print(f'Erro com os tipos de dados informados pelo usuario !')

except (ZeroDivisionError): #quando zero não e dividido
    print(f'Não é possivel dividir um número por zero !')

except(KeyboardInterrupt):
    print(f'O usuario não informou nenhum dados !')

else:
    print(f'O resultado é {r:.1f}')


finally:
    print(f'Volte sempre ! Muito Obrigado')

#vermelho
# \033[0;31mERRO ! \"{entrada}\" é um preço invalido !\033[m'


c = ('\033[m',         # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[0;30;46m',  # 6 - branco
   )