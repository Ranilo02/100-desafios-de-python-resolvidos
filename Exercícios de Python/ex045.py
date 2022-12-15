""" Crie um programa que faça o computador jogar jokenpô com você"""

"""from random import choice
p = 'pedra'
p1 = 'papel'
t = 'tesoura'
lista = [p, p1, t]
pc = choice(lista)
x = str(input('Pedra, Papel ou tesoura? '))

if x == p and pc == t or x == p1 and pc == p or x == t and pc == p1:
    print('parabéns, você escolheu \033[33m{}\033[m e o pc escolheu \033[32m{}\033[m. você venceu!'.format(x, pc));
elif x == t and pc == p or x == p and pc == p1 or x == p1 and pc == t:
    print('Você perdeu. escolheu \033[31m{}\033[m, e o PC escolheu \033[33m{}\033[m'.format(x, pc))"""

from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
PC = randint(0, 2)

# print('O computador escolheu {}'.format(itens[PC])) # lê-se "itens na posição PC"
print('''Suas opções
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? ' ))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('PC jogou  \033[34m{}\033[m'.format(itens[PC])) # lê-se "itens na posição PC"
print('jogador jogou \033[35m{}\033[m'.format(itens[jogador])) # lê-se "itens na posição jogador"
print('-==' * 11)

if PC == 0: # PC jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('PC VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif PC == 1: # PC jogou PAPEL
    if jogador == 0:
        print('PC VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif PC == 2: # PC jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('PC VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
