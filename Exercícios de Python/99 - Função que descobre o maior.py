"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa deve analisar todos os valores e dizer qual deles é o maior.
"""
# solução 1
from time import sleep

def maior(*n):

    print('-='*30)
    print('Analisando os valores passados...')
    for c in n:
        print(c, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n)}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)




# solução 2(p)

from time import sleep

def maior(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()