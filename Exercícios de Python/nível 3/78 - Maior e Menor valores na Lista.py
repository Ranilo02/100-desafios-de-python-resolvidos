"""
Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

n = []
maior = 0
menor = 0
for c in range (0, 5):
    n.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {maior} na posição ',end=' ')
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} na posição ',end='')
for i, v in enumerate(n):
    if v == menor:
        print(f'{i}...', end='')