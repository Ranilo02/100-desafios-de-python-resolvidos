"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""

resp = 'Ss'
soma = cont = média = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

média = soma/ cont
print('Você digitou {} números e soma entre eles é {}'.format(cont, soma))
print('O maior é {} e o menor {}'.format(maior, menor))
print('A média é {}'.format(média))
