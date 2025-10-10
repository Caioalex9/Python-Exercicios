pesomax = 0
pesomin = 0


for pessoa in range(1 , 6):
    peso = float(input('Peso da {} pessoa: '.format(pessoa)))
    if pessoa == 1:
        pesomax = peso
        pesomin = peso
    else:
        if peso > pesomax:
            pesomax = peso
        if peso < pesomin:
            pesomin = peso
        
print('O maior peso foi {}Kg'.format(pesomax))
print('O menor peso foi {}Kg'.format(pesomin))