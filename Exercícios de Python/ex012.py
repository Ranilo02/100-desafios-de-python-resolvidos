# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço? R$'));
d = p - (p*0.05) #ou p * 5 / 100 (o simbolo % significa resto da divisão)
print('O valor de R${} com desconto à vista de 5%, fica R${:.2f}'.format(p,d));
