"""Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer"""


#minha forma

print("""'Olá, sou seu computador...'
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")

from random import randint
c = 1
n = 1
pc = randint(0, 10)
while n != pc:
    n = int(input('Qual é o seu palpite? '))
    if n == pc:
        print('Parabéns, você acertou! você pensou {} e o PC pensou {}'.format(n, pc))
    else:
        c += 1
        if n < pc:
            print('mais... Tente outra vez')
        elif n > pc:
            print('menos... Tente outra vez')
print('Foram {} tentativas'.format(c))


#forma do professor
"""
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""


# tentei outra vez para exercitar semanas depois e consegui fazer assim:
"""
from time import sleep
from random import randint
PC = randint(0, 10)
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10. '
      'Será que você consegue adivinhar qual foi?')
sleep(2)
palpite = int(input('Qual é o seu palpite? '))
cont = 1
while palpite != PC:
    cont += 1
    if palpite < PC:
        print('Mais... Tente outra vez')
        palpite = int(input('Qual é o seu palpite? '))
    if palpite > PC:
        print('Menos... Tente outra vez')
        palpite = int(input('Qual é o seu palpite? '))
    if palpite == PC:
        print('Parabéns! Você pensou {} e o PC pensou {}'.format(palpite, PC))
        print('Você tentou {} vezes'.format(cont))

"""