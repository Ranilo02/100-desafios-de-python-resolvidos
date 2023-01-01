"""
Faça um programa que ajude um jogador da megasena a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

# solução 1
from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGAR NA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-={F" SORTEANDO {n} JOGOS "}-=-=-=')
jogo = []
for j in range(1, n+1):
    print(f'jogo {j}: ', end='')
    for c in range(0,6):
        s = randint(1, 60)
        jogo.append(s)
    jogo.sort()
    print(jogo)
    jogo.clear()
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

# solução 2 (p)

# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print(f'{"JOGA NA MEGA SENA":^30}')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' *3)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
# print('-=' *5, '< BOA SORTE! >', '-=' * 5)
