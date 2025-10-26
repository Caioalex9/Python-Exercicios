def metade(n=0, format = False):
    res = n / 2
    return res if format is False else moeda(res)

def dobro(n=0, format = False):
    res = n * 2
    return res if format is False else moeda(res)

def aumentar(n=0, taxa=0, format = False):
    """
    n vai receber um valor
    texa vai receber um valor pra taxa
    format vai formatar para real
    """
    res = n + (n * taxa / 100)
    return res if format is False else moeda(res)

def diminuir(n=0, taxa=0, format = False):
    res = n - (n * taxa / 100)
    return res if format is False else moeda(res)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.',',')


def resumo(n=0 , taxaa=10, taxar=5):

    print('-'*30)
    print('Resumo valor'.center(30))
    print('-'*30)

    print(f'Preço analisado: \t{moeda(n,)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(n, taxar, True)}')

    print('-'*30)
