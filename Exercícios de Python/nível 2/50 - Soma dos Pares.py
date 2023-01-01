"""Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daquelas que forem pares. Se o valor digitado for ímpar, desconsidere-o. """

soma = 0
for c in range(1, 7):
    n = int(input(('Digite um valor: ')))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares digitados é de {}'.format(soma))

