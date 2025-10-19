numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

c = ''

while True:
    n = int(input('Digite um número entre 0 a 20: '))

    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}')
    
    else:
        print('Valor inválido ! ',end= '')

    c = str(input('Deseja continuar?[S/N] ')).upper()
    if c in 'N':
        break

print('FIM DO PROGRAMA')