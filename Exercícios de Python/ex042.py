""" Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
 triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
EX035: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo."""


"""r1 = int(input('Qual o comprimento da primeira reta? '));
r2 = int(input('Qual o comprimento da segunda reta? '));
r3 = int(input('Qual o comprimento da terceira reta? '));

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas {} {} e {} \033[0::40m FORMAM UM TRIÂNGULO\033[m'.format(r1, r2, r3))
else:
    print('Essas retas não formam triângulo')
if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 !=r1 :
    print(' Essas retas formam um triângulo isósceles')
elif r1 == r2 == r3:
    print('formam um triângulo equilátero')
elif r1 != r2 != r3 and r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Formam um triângulo escaleno')
""""""
"""
r1 = int(input('Qual o comprimento da primeira reta? '));
r2 = int(input('Qual o comprimento da segunda reta? '));
r3 = int(input('Qual o comprimento da terceira reta? '));

# Alternativa do Guanabara com condições aninhadas:

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('as retas {} {} e {} FORMAM UM TRIÂNGULO '.format(r1, r2, r3), end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO');
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não formam um triângulo')