"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""


from time import sleep
op = 0
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
print('=-=' * 10)
print('Qual operação deseja realizar?')
while op != 5:
    print(
    """    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    op = int(input('>>>>> Sua opção: '))

    if op == 1:
        print('A soma de {} e {} é de \033[33m{}\033[m'.format(v1, v2, v1 + v2))
    elif op == 2:
        print('O resultado da multiplicação dos números é: \033[31m{}\033[m'.format(v1*v2))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor digitado foi {}'.format(v1, v2, maior))
    elif op == 4:
        print('Digite novamente os números')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        print('Fim do Programa')
    else:
        print('Opção inválida. tente novamente')
    print('=-=' * 10)
    sleep(2)


