"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a - Qual é o total gasto na compra
b - Quantos produtos custam mais de R$1000
c - Qual é o nome do produto mais caro
"""

# solução 1

total = maismil = maisbarato = cont = maisbaratonome = 0 #a variável de contagem é necessária para que seja identificada o mais barato. OBS: ela também poderia ser inicializada (ou declarada) como: maisbaratonome = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('preço R$ '))
    cont += 1
    total += preço
    if preço >= 1000:
        maismil += 1
    if cont == 1:
        maisbarato = preço  #lê- se: se for o primeiro produto, o menor preço passa a ser o preço
        maisbaratonome = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
            maisbaratonome = produto
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:10.2f}')
print(f'{maismil} produtos custam mais de R$1000')
print(f'O produto mais barato é o {maisbaratonome}, e custa R${maisbarato}')


# solução 2

total = maismil = maiscaro = maisbarato = cont = nomedoproduto = nomedoprodutomaisbarato = 0
continuar = ' '
while continuar not in 'N':
    produto = str(input('Digite o nome do produto: ')).strip().lower()
    preço = int(input(f'Digite o preço do(a) {produto} R$'))
    cont += 1
    total += preço
    if preço >= 1000:
        maismil += 1
    if cont == 1 or preço > maiscaro:
        maiscaro = preço
        nomedoproduto = produto
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomedoprodutomaisbarato = produto

    continuar = str(input('Quer continuar o cadastro? [S/N]: ')).strip().upper()[0]

print(f'O total da compra é R${total}')
print(f'{maismil} produtos custam mais de R$1000')
print(f'O nome do produto mais caro é {nomedoproduto}')
print(f'O nome do produto mais barato é {nomedoprodutomaisbarato}')

