""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida """

peso = float(input('Digite o seu peso em Kg '))
altura = float(input('Digite sua altura '))
imc = peso / (altura*altura) # ou peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc <= 18.4:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[32mParabéns! Você está com peso ideal!')
elif 25 < imc < 30:
    print('\033[30mVocê está com sobrepeso')
elif 30 < imc < 40:
    print('\033[33mVocê está com obesidade!')
else:
    print('\033[31mCUIDADO! Você está com obesidade mórbida!')