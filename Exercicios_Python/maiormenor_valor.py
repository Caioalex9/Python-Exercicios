contador = media = soma = menor = maior = 0
continuar = "S"
while continuar in 'Ss':
    numero = int(input('Digite um numero: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = str(input('Quer continuar?[S/N] ')).upper().strip()[0]

    while continuar not in ('S', 'N'):
        print('Resposta invalida ! Digite apenas S ou N')
        continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]

media = soma / contador

print('-='*30)
print('Você digitou {} números e a média entre eles foi {}'.format(contador, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('-='*30)
print('FIM')