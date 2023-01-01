"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular.
(largura e comprimento) e mostre a área do terreno.
"""

def área(larg, cump):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print(' Controle de terrenos')
print('-' * 20)
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
área(l, c)




#solução alternativa de um comentário:
def area(larg, comp):
    areaTerreno = larg * comp
    print(f'A área do terreno é {areaTerreno}m²')

print('Calculo de área do terreno.')
area(int(input('Largura do terreno: ')), int(input('Comprimento do terreno: ')))




# solução alternativa 2
def calculaárea():
    largura = float(input('LARGURA: '))
    comprimento = float(input('COMPRIMENTO: '))
    total = largura * comprimento
    print(f'A área do seu terreno é {largura} x {comprimento} que equivale a {total} m2.')

calculaárea()