"""
Faça um programa que leia a altura e largura de uma parede em metros,
calcule sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m².
"""


altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura*largura
tinta = area/2

print('A altura dessa parede é de {}m, largura de {}m e a area é de {}m², e são necessários {}L de tinta para pintá-la.'.format(altura,largura,area,tinta))