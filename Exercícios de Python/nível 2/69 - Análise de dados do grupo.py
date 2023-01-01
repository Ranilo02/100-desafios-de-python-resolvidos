"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a - Quantas pessoas têm mais de 18 anos
b - Quantos homens foram cadastrados
c - Quantas mulheres têm menos de 20 anos.
"""

"""continuar = 'Ss'
maior = homens = menos20 = 0
while continuar in 'Ss':
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
    if idade < 20 and sexo in 'Ff':
        menos20 += 1
    if sexo in 'Mm':
        homens += 1
    print('-' * 30)
    continuar = str(input('Quer continuar? '))
print(f'{maior} pessoas são maiores de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{menos20} mulheres têm menos de 20 anos')
"""


# solução do professor:

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')


