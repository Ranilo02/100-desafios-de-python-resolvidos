"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho, e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""


from datetime import date
atual = date.today().year
trabalhador = dict()
trabalhador['nome'] = str(input('Digite o nome: '))
ano = int(input('Ano de nascimento: '))
trabalhador['idade'] = atual - ano  # poderia ser date.today().year - ano ou datetime.now().year - ano (testar)
trabalhador['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = int(input('Salário R$'))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35 - atual + trabalhador['idade']
print('=-' * 30)
print(trabalhador)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')