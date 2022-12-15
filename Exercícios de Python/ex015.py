# Escreva um programa que pergunte a quantidade de Km percorridos por carro um alugado e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias foram alugados? '));
km = float(input('Quantos quilômetros foram rodados? '))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))
