'''Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com sua idade:
- se ele ainda vai se alistar no serviço militar
- se é hora de se alistar
- se já passou do tempo do alistamento.
Seu programa também deve mostrar o tempo que falta ou que passou de prazo.'''

"""ano = int(input('Qual a sua idade? '))
if ano <= 16:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - ano));
elif ano == 17:
        print('Ainda falta 1 ano para o seu alistamento');
elif ano == 18:
    print('Apresente-se no QG mais próximo. Está na hora de se alistar no serviço militar');
elif ano == 19:
        print('Já passou 1 ano do prazo do alistamento, por favor informe-se no QG mais próximo');
elif ano > 19:
    print('Já passou {} anos do prazo do alistamento, por favor informe-se no QG mais próximo'.format(ano - 18));"""

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!');
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo));
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano));

#alternativa: em vez de "ano = atual +/- saldo", achei melhor colocar ano = nascimento + 18, dá no mesmo, mas ajuda na visualização
