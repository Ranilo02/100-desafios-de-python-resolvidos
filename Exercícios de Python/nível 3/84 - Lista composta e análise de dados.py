"""
Faça um programa que leia o nome e peso da várias pessoas, guardando tudo em uma lista. No final, mostre:

a- Quantas pessoas foram cadastradas
b- Uma listagem com as pessoas mais pesadas
c- Uma listagem com as pessoas mais leves
"""

princ = list()
temp = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continuar? [S/N]: '))
    if resp in 'Nn':
        break

print(f'Esses são os dados {princ}')
print(f'Foram registradas {len(princ)} pessoas.')

print(f'O maior peso foi {mai}Kg. Peso de ',end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi {men}Kg. Peso de ',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')


# Dica que vi nos comentários:

# for nome, peso in princ:
#     if peso == mai:
#         print(f'O mais pesado é {nome}', end='')
# for nome, peso in princ:
#     if peso == men:
#         print(f'O mais leve é {nome}', end='')