tuplas = ('Aprender', 'Programar', 'Linguaguem','Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

print('-='*30)
print('{:^60}'.format('Contando Vogais de palavras nas tuplas'))
print('-='*30)

for palavra in tuplas:
    print(f'\nNa palavras {palavra.upper()} temos: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



