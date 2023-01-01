"""
Crie um algoritmo que mostre seu dobro, triplo e raiz quadrada.
"""


n = int(input('Digite um valor'));
print('o valor {} tem seu dobro {}, triplo {} e sua raíz quadrada {:.2f}'.format(n, n*2, n*3, n**(1/2)))


#OBS: no lugar de "n**(1/2)" poderia ser "pow(n,(1/2))", pois essa é outra forma de fazer exponenciação
