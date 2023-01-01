"""Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar"""

número = int(input('Digite um número: '))
resto = número % 2
if resto == 0:
    print('o número é par')
else:
    print('O número é ímpar')