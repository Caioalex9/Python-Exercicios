numero = cont = soma = 0
numero = int(input('Digite um valor:[999 para PARAR] '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um valor:[999 para PARAR] '))
print('~'*30)
print('Você digitou {} numeros e a soma entre eles é {}'.format(cont, soma), end='')
print(' -> FIM')