"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
a - quantas pessoas foram cadastradas
b - A média de idade do grupo
c - Uma lista com todas as mulheres
d - Uma lista com todas as pessoas com idade acima da média
"""

# solução 1

# pessoa = dict()
# pessoas = []
# mulheres = []
# idade_acima = []
# somaidade = 0
# sexo = ''
# continuar = 'Ss'
# while continuar not in 'Nn':
#     pessoa['nome'] = str(input('Nome: '))
#     sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
#     if sexo not in 'MmFf':
#         while sexo not in 'MmFf':
#             print('Erro! Por favor, digite apenas M ou F.')
#             sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
#     if sexo in 'MmFf':
#         pessoa['sexo'] = sexo
#     if sexo == 'F':
#         mulheres.append(pessoa['nome'])
#     pessoa['idade'] = int(input('Idade: '))
#     somaidade += pessoa['idade']
#     pessoas.append(pessoa.copy())
#     continuar = str(input('Continuar? [S/N]: '))
#     if continuar not in 'SsNn':
#         while continuar not in 'SsNn':
#             print('ERRO! Por favor, Responda apenas S ou N.')
#             continuar = str(input('Continuar? [S/N]: '))
# print('-='*30)
# print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
# print(f'B) A média de idade é de {somaidade / len(pessoas):.2f} anos.')
# print('C) As mulheres cadastradas foram: ',end='')
# for c in mulheres:
#     print(f'{c}', end=' ')
# print()
# for k, v in enumerate(pessoas):
#     if v["idade"] > (somaidade/len(pessoas)):
#         idade_acima.append(v)
# print('D) Lista de pessoas com idade acima da média: ')
# for c in idade_acima:
#     print(f'    nome = {c["nome"]};',f'sexo = {c["sexo"]};', f'idade = {c["idade"]};')
# print('<< ENCERRADO >>')



# solução 2

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')    # poderia ter só colocado um end='' na linha 87 no print das pessoas acima da média de idade
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')