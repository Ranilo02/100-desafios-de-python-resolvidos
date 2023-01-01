"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.
"""

# minha solução

vinte = 0
print('='*30)
print('{:30}'.format('BANCO CABRAL'))
print('='*30)

n = int(input('Qual valor você quer sacar? R$ '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

if d % 2 == 0: vinte = d / 2
else: vinte = (d - 1) / 2
um = u
dez = d % 2
cinquenta = m * 20 + c * 2

print('Total de: ')
print(f'{cinquenta} cédulas de R$50') if cinquenta > 0 else ''
print(f'{vinte:.0f} cédulas de R$20') if vinte > 0 else ''
print(f'{dez} cédulas de R$10') if dez > 0 else ''
print(f'{um} cédulas de R$1') if um > 0 else ''



# solução do professor


print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50: #se a cédula atual for igual a 50, então não posso mais tirar 50 do valor total, então a próxima vai virar 20
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0  # lembrando que o totcéd é o contador, cada vez que muda a cédula tem que reiniciar a contagem
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV" Tenha um bom dia!  ')