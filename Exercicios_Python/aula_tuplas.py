from time import sleep

# .index busca um item na posição
# sorted organiza por ordem alfabetica
# count conta quantas vezes aparece
# len conta os itens na lista
# reverse=true inverter os valores

#Tuplas sao IMUTAVEIS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita', 'Milkshaker', 'Agua com gás', 'Gelo e Limão')

# print(sorted(lanche))

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
#     sleep(1)

# for cardapio in range(0, len(lanche)):
#     print(f'Qual lanche você gostaria de pedir ? {lanche[cardapio]} [ ] {cardapio}')
    

for pos, comida in enumerate(lanche):
    print('-='*20)
    if comida == 'Suco' or comida == 'Milkshaker' or comida == 'Agua com gás':
        print(f'Eu vou tomar {comida}, na posição {pos}')
        sleep(2)
        if comida == 'Agua com gás':
            Gelolimao = print(input('Você gostaria de Gelo e limão?[S/N] '))
            if Gelolimao == 'Ss':
                continue
            else:
                break
        print('Hummm...Gostoso !')
        sleep(1)

    else:     
        print(f'Eu vou comer {comida}, na posição {pos}')
        sleep(2)
        print('Hummm...Gostoso!')
        sleep(1)

print('-='*20)
print('Estou cheio, comi', len(lanche),'lanches')