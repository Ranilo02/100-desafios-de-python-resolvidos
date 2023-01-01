"""
Faça um programa um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
que ele conquistou no final o jogo.
"""
""""

# solução 1

from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
cont = 0
while True:
    v = int(input('Diga um valor: '))
    p = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0, 11)
    total = pc + v
    par = total % 2 == 0
    impar = total % 2 != 0

    if p in 'P' and par:
        print(f'Você jogou {v} e o computador jogou {pc}. total {total} deu PAR')
        print('Você Venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    elif p in 'I' and impar:
        print(f'Você jogou {v} e o computador jogou {pc}. total {total} deu ÍMPAR')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    elif p in 'I' and par:
        print(f'Você jogou {v} e o computador jogou {pc}. total {total} deu PAR')
        print('Você perdeu!')
        break
    elif p in 'P' and impar:
        print(f'Você jogou {v} e o computador jogou {pc}. total {total} deu ÍMPAR')
        print('Você perdeu!')
        break
    print('=-'*30)
print(f'GAME OVER. Você conquistou {cont} vitórias consecutivas')
"""

# solução 2 (professor)

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {v} vezes.')

# tentativa semanas depois 07/10/2022

from random import randint
vit = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-' * 15)
while True:
    jogador = str(input('Par ou Ímpar? [P/I] ' )).upper().strip()[0]
    valor = int(input('Diga um valor de 0 a 10: '))
    pc = randint(0, 10)
    resultado = valor + pc
    if resultado % 2 == 0:
        print('-' * 20)
        print(f'Você jogou {valor} e o computador jogou {pc}. total de {resultado} Deu PAR')
        print('-' * 20)
        if jogador == 'P':
            print('VOCÊ VENCEU!')
            print('-'*20)
            vit += 1
        else:
            print('VOCÊ PERDEU!')
            break
            print('-'*20)

    else:
        print(f'Você jogou {valor} e o computador jogou {pc}. total de {resultado} Deu ÍMPAR')
        if jogador == 'I':
            print('VOCÊ VENCEU!')
            print('-'*20)
            vit += 1


        else:
            print('VOCÊ PERDEU!')
            print('-'*20)
            break
    print('Vamos jogar novamente...')
print('-' * 60)
print(f'GAME OVER! Você conquistou {vit} vitórias consecutivas')
print('=-' * 60)
