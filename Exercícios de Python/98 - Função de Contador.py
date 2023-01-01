"""
Faça um programa que tenha uma função chamada contador(), que receba trÊs parâmetros: início, fim e passo
e realize a contagem. Seu programa deve realizar três contagens através da função criada:
a) De 1 até 10, de um em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""

# solução 1

# from time import sleep
# def contador():
#     print('-='*20)
#     print('Contagem de 1 até 10 de 1 em 1')
#     sleep(0.2)
#     for c in range(1,11):
#         print(c,end=' ')
#         sleep(0.3)
#     print('FIM!')
#     print('-=' * 20)
#     print('Contagem de 10 até 0 de 2 em 2')
#     sleep(1)
#     for c in range(10, -2, -2):
#         print(c, end=' ')
#         sleep(0.3)
#     print('FIM!')
#     print('-=' * 20)
#     sleep(1)
#     print('Agora é sua vez de personalizar a contagem!')
#     i = int(input('Início: '))
#     f = int(input('Fim:    '))
#     p = int(input('Passo:  '))
#     if p < 0: p = p*(-1)
#     if p == 0: p = p+1    # ou p = 1
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     print('-=' * 20)
#     sleep(1)
#     if f < i or p < 0:
#         for c in range(i, f-1, -p):
#             print(c,end=' ')
#             sleep(0.2)
#         print('FIM!')
#     if f > i:
#         for c in range(i, f, p):
#             print(c,end=' ')
#             sleep(0.2)
#         print('FIM!')
#
# contador()
#
#


# solução 2(p)

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)  # o flush serve para tornar o programa fluído, caso ele não esteja se comportando assim.
            #sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end=' ', flush=True)
            #sleep(0.5)
            cont -= p
        print('FIM!')


contador(10, 1, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)