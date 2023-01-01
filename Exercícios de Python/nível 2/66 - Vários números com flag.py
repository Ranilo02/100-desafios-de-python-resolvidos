"""
Crie um programa que leia vários númeos inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
"""

n = s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números, e a soma entre eles é {s}')