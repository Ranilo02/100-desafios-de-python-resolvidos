"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá deverá escrever na tela se o usuário venceu ou perdeu."""

# solução 1
import random
número = int(input('escolha um número de 0 a 5: '))
sorteado = random.randint(0,5)
if número == sorteado:
    print('Parabéns! você venceu')
else:
    print('sinto muito, mas você perdeu...')


# solução 2
from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('Ganhei, vacilão! eu pensei no número {}, não no número {}'.format(computador, jogador))