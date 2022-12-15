''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal '''

num = int(input('Digite um número inteiro: '));
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO'
[ 2 ] converter para OCTAL'
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('sua opção: '));
if opção == 1:
    print('o número \033[33m{}\033[m convertido para BINÁRIO é \033[34m{}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('o número \033[33m{}\033[m convertido para OCTAL é \033[34m{}\033[m '.format(num, oct(num)[2:]))
elif opção == 3:
    print('o número \033[33m{}\033[m convertido para HEXADECIMAL é \033[34m{}\033[m '.format(num, hex(num)[2:]))
else:
    print('opção inválida. tente novamente')

