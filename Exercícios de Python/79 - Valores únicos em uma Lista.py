"""
Crie um programa onde o usuário pode digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

números = list()
continuar = 'Ss'
while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('---Adicionado com sucesso---')
    else:
        print('>>Valor duplicado. Não será adicionado<<')
    continuar = input('Quer continuar: [S/N] ').strip().lower()[0]
números.sort()
print(f'Você digitou os valores {números}')