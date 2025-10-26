def linha(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

def area():
    linha('   Controle de terrenos')

    largura = float(input('Largura do terreno: '))
    comprimento = float(input('Comprimento do terreno: '))
    area = largura * comprimento
    print(f'A area do terreno de {largura}x{comprimento} é {area}m²')


#programa principal

area()