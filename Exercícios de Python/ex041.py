"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
 atleta e mostre sua categoria, de acordo com a idade:
 - Até 9 anos: Mirim
 - Até 14 anos: Infantil
 - até 19 anos: Junior
 - Até 25 anos: Sênior
 - Acima: master"""

from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta? '))
idade = ano - nascimento
if idade <= 9:
    print('O atleta tem \033[31m{} anos\033[m, categoria \033[31mMIRIM'.format(idade))
elif idade >= 10 and idade <=14 : #você pode cortar o trecho idade >= 10 e deixar apenas idade <= 14, pois o if anterior já impõe por tabela essa condição de ser <=10
    print('O atleta tem \033[36m{} anos\033[m, categoria \033[36mINFANTIL'.format(idade))
elif idade >= 15 and idade <= 19:
    print('O atleta tem \033[32m{} anos\033[m, categoria \033[32mJUNIOR'.format(idade))
elif idade == 20:
    print('O atleta tem \033[35m20 anos\033[m, categoria \033[35mSÊNIOR')
else:
    print('O atleta tem \033[30m{} anos\033[m, categoria \033[30mMASTER\033[m'.format(idade))

#alternativa
"""
if idade <=9
elif <=14
elif <= 19
elif <= 25
else:
"""
