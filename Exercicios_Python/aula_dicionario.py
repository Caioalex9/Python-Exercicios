filme = {'titulo':'Star Wars', 
         'ano': 1977,
         'diretor':'George Lucas'}

# Comandos
# .copy() usado no dicionario para salvar a copia 


print(filme.values()) #retorna os valores do dicionario. parte de cima
print(filme.keys()) #retorna as chaves do dicionario. ex: 'nome','idade' parte de baixo
print(filme.items())#retorna tudo do dicionario. retorna valor e chave

for k, v, in filme.items():
    print(f'O {k} é {v}')


estado = dict()
brasil = list()

for c in range (0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')