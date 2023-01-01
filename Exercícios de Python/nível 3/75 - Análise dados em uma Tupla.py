"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a- Quantas vezes apareceu o valor 9.
b- Em que posição foi digitado o primeiro valor 3.
c- Quais foram os números pares.
"""

tupla = (int(input(f'Digite um número: ')),
     int(input(f'Digite outro número: ')),
     int(input(f'Digite mais um número: ')),
     int(input(f'Digite o último número: ')))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
tres = tupla.count(3)
if tres > 0: # isso poderia ser substituído por ➝  if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
