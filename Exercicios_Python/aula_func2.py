# COMANDOS
# """""" # em baixo do def voce cria documentação da função
#.__doc__ # documentação do comendo 

def somar(a, b, c=0):
    """
    Função para somar valores
    """
    soma = a + b + c
    return soma

def fatorial(num = 1):
    """
    Função para fatorial de um numero
    """
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

def par(nu=0):
    """
    Função para descobrir se o numero é PAR
    """
    if n % 2 == 0:
        return True
    else:
        return False



r1 = somar(3,7)
r2 = somar(6,10)
r3 = somar(3,8)

print(f'A soma dos valores é {r1}')

n = int(input('Digite um valor pro fatorial: '))
print(f'O fatorial de N é igual a {fatorial(n)}')


nu = int(input('Digite um número: '))
if par(nu):
    print(f'É Par !')
else:
    print(f'Não é PAR')

