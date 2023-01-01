"""Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo."""

r1 = float(input('comprimento da primeira reta: '))
r2 = float(input('comprimento da segunda reta: '))
r3 = float(input('comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, as três retas formam um triângulo')
else:
    print('Não formam um triângulo')