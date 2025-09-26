Peso = float(input('Qual é o seu PESO?(KG) '))
Altura = float(input('Qual é a sua altura?(M) '))

IMC = Peso / (Altura ** 2)

print('Seu IMC é {:.1f}'.format(IMC))

if IMC <= 18.5:
    print('Abaixo do peso')
elif IMC <= 25:
    print('Peso Ideal')
elif IMC <= 30:
    print('Sobrepeso')
elif IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')