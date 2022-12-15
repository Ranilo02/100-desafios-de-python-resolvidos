"""
Refaça o desafio 51, lendo o primeiro termo e a Razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutra while.
"""

print('Gerador de PA')
print( '=-' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{}→ '.format(termo), end='')
    cont += 1
    termo += razão
print("FIM")
