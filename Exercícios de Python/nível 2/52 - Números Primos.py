"""Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo"""


n = int(input('Digite um número: '))
tot = 0
for c in range (1, n+1): #vai do número 1 até o número(n) pra ver por quantos ele vai dividir
    if n % c == 0: #lê-se: se o número(n) for divisível pelo contador:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\033[m O número {} foi dividido {} vezes.'.format(n, tot))
if tot == 2:
    print('Portanto ele é PRIMO')
else:
    print('Portanto ele NÃO É PRIMO')
