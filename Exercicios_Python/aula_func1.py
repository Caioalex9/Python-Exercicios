
# #funcao sem parametro
# def linha():
#     print('-='*30)

# linha()


# #funcao com parametro
# def titulo(txt): #passo o parametro no exemplo de txt
#     print('-='*30)
#     print(txt) #retorna o valor que está dentro da funçao
#     print('-='*30)

# def som(a, b):
#     s = a + b
#     print(f'a soma de {a} + {b} é {s}')

# valores =[7,2,5,0,4]

# def dobra(lst):
#     pos = 0
#     while pos <len(lst): #listas 
#         lst[pos] *= 2
#         pos += 1
#     print(valores)


# dobra(valores)

def soma(* valores): # uso do * para pegar varios valores desempacotamento 
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


# #PROGRAMA PRINCIPAL

# titulo('Curso em video') #comando criado por meio de funçao
# titulo('PYTHON É MUITO BOM') #retorna valor dentro do comando com parametros

# som(4, 5)
# som(8, 9)
# som(2, 1)

soma(5, 9)
soma(3, 7, 5, 7)