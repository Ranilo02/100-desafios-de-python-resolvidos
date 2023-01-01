""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele usando métodos """



a = input('digite algo: ')
print(f'O tipo primitivo desse valor é: {type(a)}') # sempre vai ser str, porque o input não está especificado.

b = str(input('Digite algo: '))
print(f'O tipo primitivo desse valor é: {type(b)}')
print(f'Só tem espaços: {b.isspace()}') # só tem espaço?
print(f'É um número? {b.isnumeric()}')
print(f'É alfabético? {b.isalpha()}')  # só letras?
print(f'É alfanumérico? {b.isalnum()}')
print(f'Está em maiúsculas? {b.isupper()}')
print(f'Está em minúsculas? {b.islower()}')
print(f'Está capitalizada? {b.istitle()}')

