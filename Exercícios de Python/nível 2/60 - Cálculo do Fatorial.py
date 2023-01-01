"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5!5x4x3x2x1 = 120
"""


# forma direta com módulo de fatorial
"""from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))"""

# forma padrão

"""n = int(input('Digite um número para que seja calculado seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')"""

# forma em laço for
n = int(input('Digite um número para que seja calculado seu fatorial: '))
f = 1
print('calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    if c > 0:
        print(c, ' x ' if c > 1 else ' = ', end=' ')
        f *= c
print(f, end='')
