"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
n = 0
soma = 1
while n != 999:
    n += n
    n = int(input('digite um número [999 para parar]:  '))
print('A soma dos números é de {}'.format(n))