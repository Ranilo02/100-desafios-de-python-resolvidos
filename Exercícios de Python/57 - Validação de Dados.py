"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

s1 = 0
s = str(input('Informe o seu sexo [M/F] ')).strip().upper()[0]
while s == s != 'M' and s != 'F':  #coloquei assim em vez de while s not in 'MmFf', Porque se a pessoa colocar qualquer valor começando com M ou F, o programa vai aceitar, abrindo margem para quem digitar sem querer, tipo 'fhbjvmc'  ou 'mwefsa'.
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(s))


# tentei de novo quase 1 mês depois e fiz assim:
""" 
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor Digite seu sexo: ')).strip().upper()[0]
if sexo in 'Mm':
    print('Você é do sexo masculino')
elif sexo in 'Ff':
    print('Você é do sexo feminino.')
"""

