times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'São Paulo', 'Bragantino', 'Ceará', 'Vasco', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Internacional', 'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')

print('-='*30)

print(f'Listas de times do Brasileirão: {times}')

print('-='*30)

print(f'Os cincos primeiros colocados foram {times[0:5]}')

print('-='*30)

print(f'Os últimos 4 colocados na tabelas foram {times[-4:]}')

print('-='*30)

print(f'Times em ordem alfabetica {sorted(times)}')

print('-='*30)

print(f'O Vasco está na {times.index('Vasco')+1}ª posição')

