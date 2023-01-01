"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

# solução 1

lista = []
listaP = []
listaI= []
continuar = 'Ss'
while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listaP.append(n)
    elif n % 2 == 1:
        listaI.append(n)
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
print(lista)
print(listaP)
print(listaI)



# solução 2 (melhor, com análise de pares e impares da lista já criada)

num = []
pares = []
impares = []

while True:
    num.append = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
