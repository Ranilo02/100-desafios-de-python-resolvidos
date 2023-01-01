'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
ou então o empréstimo será negado.'''

print('Bem-vindo ao Ranilo Empréstimos, vamos começar a consulta?')
pc = float(input('Qual o preço da casa? R$ '))
sal = float(input('Qual a sua renda mensal? R$ '))
prazo= int(input('Em quantos anos pretende quitar a casa? '))

if pc / (prazo * 12) <= sal * 30/100:
    print('Seu empréstimo foi aprovado')
else:
    print('Lamentamos, mas seu empréstimo foi negado')

# alternativa que criei na segunda vez que fiz: if (sal - (sal * 70/100)) < casa / (tempo * 12):