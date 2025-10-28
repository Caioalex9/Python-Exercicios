from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Novas Pessoas','Sair do sistema'])

    if resposta == 1:
        #função de listar pessoas no arquivo
        lerArquivo(arq)

    elif resposta == 2:
        #Opção cadastrar pessoas
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('SAINDO DO SISTEMA... ATE LOGO !')
        break
    
    else:
        print('\033[0;31mERRO ! Selecione uma OPÇÃO VALIDA.\033[m')
    sleep(2)