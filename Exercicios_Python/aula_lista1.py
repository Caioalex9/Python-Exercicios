# lanche = ['cachorro quente', 'hamburgue', 'suco', 'pizza', 'picole', 'cookie']
# print(lanche)

# num = [2,5,9,1]
# print(num)

valores = []

# a = [2, 3, 4, 7]
# b = a[:] #[:] Fazer uma copia da lista, Sem faz uma ligação e da blayblade
# b[2] = 8
# print(f'Lista A : {a}')
# print(f'Lista B: {b}')


# COMANDOS

# .index busca um item na posição
# sorted organiza por ordem alfabetica
# count conta quantas vezes aparece
# len conta os itens na lista
# reverse=true inverter os valores

#LISTAS SÃO MUTAVEIS

#Adicionar valores

# lanche.append('Batata frita')
# lanche.insert()

# num[2] = 3 #adiciona o 3 no lugar do 9
# num.append(7) #adiciona o 7 como ultimo item da lista
# num.sort(reverse=True) #inverte os valores da lista
# num.insert(2, 2) #adiciona na 2º casa o um dado 

#Para remover dados:

#del lanche [3]
#lanche.pop(3)
#lanche.remove('pizza')

# if 4 in num: #Verifica se o item ta na lista para não dar ERRO 
#     num.remove(4)
# else:
#     print('Não achei o número 4')

#num.remove(2) #remove o 1 elemento da busca
#num.pop(2) #Remove o dado da 2º casa 'vazio remove o ultimo'

#Verificar se PIZZA ta na lista

# if 'pizza' in lanche:
#     lanche.remove('pizza')

# print(lanche)

# print(num)
# print(f'Essa lista tem {len(num)} elementos.') #conta a quantidade de elemento

#funçao LIST

#valores = list(range(4,11)) #Criando lista ordenada
# valores = [8,2,5,4,9,3,0] #lista desordenada...padrão
# valores.sort() #.sort para organizar
# valores.sort(reverse=True) # reverse=True mostrar lista ao contrario
# print(valores)


for pergunta in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for contador, valor in enumerate(valores):
    print(f'Na Posição {contador} encontrei o valor {valor}!')

print('Cheguei ao fim da lista.')


