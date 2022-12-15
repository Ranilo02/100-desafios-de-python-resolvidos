""""""# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa
# Guanabara adicionou mais uma variável para não usar o módulo: hi = (co**2 + ca**2) **(1/2)
# já eu fiz com o módulo, e ficou assim no import: .format(co,ca, math.sqrt((co**2)+(ca**2))))

"""
co = int(input('Comprimento do cateto oposto: '))
ca = int(input('comprimento do cateto adjascente: '))
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa desse retângulo é {}'.format(int(hi)))
"""

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h1 = hypot(co, ca)
print('O triângulo retângulo tem os comprimentos de {} de cateto oposto, {} adjacente e {:.2f} sua hipotenusa'.format(co, ca, h1))

