"""Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente"""



#solução 1
nome = str(input('Escreva seu nome completo: ')).strip().lower()
separado = nome.split()
print('o primeiro nome é {} e o último nome é {}'.format(separado[0], separado[-1]))


#solução 2
nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('Muito prazer, {}'.format(separado[0]))
print('Então você é da família {}'.format(separado[len(separado)-1]))