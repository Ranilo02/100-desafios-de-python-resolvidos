"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e condição de pagamento:
- À vista dinheiro ou cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

"""valor = float(input('Qual o preço do produto? '));
print('          *****FORMA DE PAGAMENTO***** \n -pagamento à vista dinheiro ou cheque (10% de desconto): tecle [1]\n '
      '-À vista no cartão (5% de desconto) tecle [2]\n '
      '-Em até 2x no cartão (preço normal) tecle [3]\n ' 
      '-3x ou mais no cartão (20% de juros) tecle [4]\n ')

fp = int(input('Escolha a forma de pagamento: '))

if fp == 1:
      print('*pagamento à vista com 10% de desconto*.\n Sua compra sairá por R${:.2f}'.format(valor - (valor * 10/100)))
elif fp == 2:
      print('pagamento à vista no cartão com 5% de desconto.\n Sua compra sairá por R${:.2f}'.format(valor - (valor * 5/100)))
elif fp == 3:
      print('pagamento em 2x no cartão R$\033[33m{:.2f}'.format(valor));
elif fp == 4:
      print('pagamento a partir de 3x no cartão (20% de juros) total de R$\033[32m{:.2f}'.format(valor + (valor * 20/100)));
else:
      print('\033[31mDigite uma das opções válidas')"""

print ('{:=^40}'. format(' LOJAS GUANABARA' ))
preço = float(input('Preço das compras R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro ou cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] Em até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros) tecle''')

opção = int(input('Qual a opção? '))
if opção == 1:
      total = preço - (preço * 10/100)
elif opção == 2:
      total = preço - (preço * 5/100)
elif opção == 3:
      total = preço
      parcela = preço / 2
      print('Sua compra será parcelada em 2x de {}'.format(parcela))
elif opção == 4:
      total = preço + (preço * 20/100)
      totparc = int(input('escolha em quantas vezes pretende dividir: '))
      print('Suas compras serão divididas em {}x de R${:.2f} COM JUROS '.format(totparc, total / totparc))
else:
      total = preço
      print('Opção inválida. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))
