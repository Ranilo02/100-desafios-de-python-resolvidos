"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla.
"""


# solução 1:
"""
from random import randint
maior = menor = 0
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
números = n1,n2,n3,n4,n5
maior = menor = sorted(números)
print(f'os valores sorteados foram ', end= '')
for cont in números:
    print(cont, end='')
print(f'\nO maior número é o {maior[-1]}')
print(f'O menor número é o {menor[0]}')
"""

# solução 2:

from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for n in números:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')

