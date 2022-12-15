# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (cotação do dólar R$5,19)

real = float(input('Digite o valor em real R$'));
dólar = real/5.19
print('O valor de R${} convertido para dólar fica US${:.2f}' .format(real,dólar));
