"""
Crie um programa que vai ler vários números e colocá-los em uma lista.
Depois disso, msotre:
A- Quantos números foram digitados
B- A lista de valores ordenada de forma descrescente.
C- Se o valor 5 foi digitado e está ou não na lista.
"""


# solução 1

lista = list()
continuar = 'Ss'
c = 0
while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
print(f'Foram digitados {c} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são {lista}')
if lista.count(5) > 0:
    print(f'O valor 5 foi encontrado na lista na posição ',end='')
for i, v in enumerate(lista):
    if v == 5:
        print(f'{i}...',end='')
if lista.count(5) == 0:
    print('Não foi encontrado o valor 5')

# solução 2 (prof)

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
