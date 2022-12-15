"""Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos dígitos separados.
 ex: 1834
 unidade: 4
 dezena: 3
 centena: 8
 milhar: 1 """

n = int(input('Digite um número de 4 dígitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('unidade: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhar: {}'.format(m))



