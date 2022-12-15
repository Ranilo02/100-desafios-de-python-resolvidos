# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%.

s = int(input('Digite seu salário: '));
a = s*0.15 #ou fazendo direto: a + (a * 15 / 100)
ns = s+a

print('O salário de R${}, sofreu um aumento de 15%, ou seja R${}, agora o novo valor é de R${}'.format(s,a,ns));

