"""Escreva um programa que pergunte qual o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%."""

'''sal = float(input('Digite o valor do salário: '))
dez = (sal * 10/100) + sal
quinze = (sal * 15/100) + sal
if sal >= 1250.01:
    print('Seu aumento é de 10%, passando a ser: {:.2f}'.format(dez))
else:
    print('Seu aumento é de 15%,passando agora a ser de {:.2f}'.format(quinze))'''

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('O salário de {:.2f} passa a ser de {:.2f}'.format(salário, novo))
