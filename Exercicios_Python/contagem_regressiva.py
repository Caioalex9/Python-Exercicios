import time

print('Contagem regressiva para os estouros dos fogos !')
for c in range(10, -1, -1):
    time.sleep(1)
    print('{}...'.format(c))
print('FOGOS EXPLODINDO !! ')
