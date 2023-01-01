"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""


números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
continuar = 'Ss'
while continuar in 'Ss':
    while True:
        escolha = int(input('Digite um número entre 0 e 20: '))
        if 0 <= escolha <= 20:
            break
        print('Tente novamente. ', end='')
    print('=' * 24)
    print(f'Você digitou o número {números[escolha]}')
    print('=' * 24)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
