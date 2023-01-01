"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
Calcule e mostre o comprimento da hipotenusa
"""

#solução 1
co = int(input('Comprimento do cateto oposto: '))
ca = int(input('comprimento do cateto adjascente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa desse retângulo é {}'.format(int(hi)))


#solução 2
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h1 = hypot(co, ca)
print('O triângulo retângulo tem os comprimentos de {} de cateto oposto, {} adjacente e {:.2f} sua hipotenusa'.format(co, ca, h1))

