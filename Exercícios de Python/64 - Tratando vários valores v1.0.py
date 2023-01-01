"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""


núm = soma = cont = 0
núm = int(input('Digite um número [999 para parar]:  '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]:  ')) #o flag (999) não vai entrar na soma estando nessa sequência
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
