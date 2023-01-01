"""Crie um programa um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1

    else:
        menor += 1
print('{} pessoas já atingiram a maioridade'.format(maior))
print('{} pessoas ainda não atingiram a maioridade'.format(menor))
