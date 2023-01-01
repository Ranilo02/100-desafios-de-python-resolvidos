"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a- Apenas os cinco primeiros colocados.
b- Os últimos 4 colocados na tabela.
c- Uma lista com os times em ordem alfabética
d- Em que posição na tabela está o time da Chapecoense.
"""

print('-='*15)
times = 'Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corithians', 'Internacional', 'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminese', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória'
print(f'Lista de times do brasileirão {times}')
print('-='*15)
print(f'Os cinco primeiros colocados são {times[0:5]}')
print('-='*15)
print(f'Os quatro últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'O Vitória está na {times.index("Vitória")+1}ª posição')
for pos, cont in enumerate(sorted(times)):
        print(pos+1, cont)