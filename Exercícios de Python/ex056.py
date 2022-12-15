minha forma de resolver:
"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre:
 - A média de idade do grupo
 - o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos """

mais_velho = 0
somaidade = 0
homem = 0
menos20 = 0
for cidadão in range (1, 4+1):
    nome = str(input('Escreva o nome da {}ª pessoa: '.format(cidadão)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(cidadão)))
    somaidade += idade
    gênero = int(input("""Digite o sexo da {}ª pessoa
[1] masculino 
[2] feminino
sua opção: """.format(cidadão)))
    if gênero == 1:
        if cidadão == 1:
            homem = idade
            mais_velho = nome
        else:
            if idade > homem:
                homem = idade
                mais_velho = nome
    else:
        if idade < 20:
            menos20 += 1

print('A média de idade do grupo é de {:.0f} anos'.format(somaidade/ 4))
if gênero == 1:
    print('O nome do homem mais velho é {}'.format(mais_velho))
if menos20 > 1:
    print('{} mulheres têm menos de 20 anos'.format(menos20))
else:
    if menos20 == 1:
        print('{} mulher têm menos de 20 anos'.format(menos20))

forma do Guanabara:
"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre:
 - A média de idade do grupo
 - o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos """

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}a PESSOA -----'.format(p))
    nome = str(input('nome: ')).strip()
    idade =(int(input('idade: ')))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade/4
print('A média de idade do grupo é {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))