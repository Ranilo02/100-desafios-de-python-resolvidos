"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas minúsculas
-Quantas letras ao todo (sem considerar espaço)
-Quantas letras tem o primeiro nome
"""


nome = str(input('Digite seu nome: ')).strip()
print('seu nome em maiusculas é: {}'.format(nome.upper()))
print('seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {}'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

