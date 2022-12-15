"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA
(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.
"""
# forma do professor
"""print('='*30)
print('     10 TERMOS DE UMA PA     ')
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range (primeiro, décimo + razão, razão):
    print(c, end=' → ')
print('ACABOU')"""

# minha forma (melhor)

início = int(input('primeiro termo: '))
razão = int(input('Razão: '))
décimo = início + 10 * razão   # forma dele: "primeiro + (10 -1) * razão"
for c in range(início, décimo, razão):    # forma dele "primeiro, décimo + razão, razão"
    print(c, end=' ->')
print('FIM')

