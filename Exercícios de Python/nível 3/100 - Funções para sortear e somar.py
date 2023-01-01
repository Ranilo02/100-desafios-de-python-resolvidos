"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior.
"""

# solução 1

from random import randint
from time import sleep

números = list()


def sorteia():
    for c in range(0, 5):
        v = randint(0, 10)
        números.append(v)
    print('Sorteando 5 valores da lista: ', end='')
    for c in números:
        print(c, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {números}', end=' ')
    for i in números:
        if i % 2 == 0:
            soma += i
    print(f'Temos {soma}')


sorteia()
somaPar()



# solução 2(p)

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista. ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)