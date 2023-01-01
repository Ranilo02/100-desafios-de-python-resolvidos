"""Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
 so que agora utilizando um laço for."""

multiplicador = int(input('Digite o número que você quer a tabuada:  '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(multiplicador, c, multiplicador * c))