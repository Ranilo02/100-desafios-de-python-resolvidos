"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
ex:
Escreva (Olá, Mundo!)
saída:
----------
Olá,Mundo!
----------
"""

# solução 1
# def escreva(msg):
#     print('~~',end='')
#     print('~'*len(msg),end='~~')
#     print(f'\n  \033[34m{msg}\033[m')
#     print('~~',end='~~')
#     print('~'*len(msg))
#
#
# while True:
#     escreva(input('Digite algo: '))



# solução 2(p)
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Ranilo Cabral')
escreva('Curso de Python')
escreva('CeV')
