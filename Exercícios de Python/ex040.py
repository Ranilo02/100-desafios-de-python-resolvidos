"""Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5 e 6.9: recuperação
- média 7.0 ou superior: aprovado """

n1 = float(input('Digite a primeira nota: '));
n2 = float(input('Digite a segunda nota: '));
if (n1 + n2)/2 <= 4.9:
    print('\033[31mO aluno está reprovado')
elif (n1 + n2)/2 >= 5 and (n1 + n2)/2 <= 6.9 :
    print('\033[33mO aluno está de recuperação')
else:
    print('\033[32mO aluno está aprovado')

# alternativa: criar a variável média e usar "if 7 > média >=5"