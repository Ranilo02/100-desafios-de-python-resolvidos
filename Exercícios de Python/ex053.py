"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo"""

"""algoritmo:
1 - digitar a frase, já eliminando os espaços laterais e jogando a frase para maiúsculo.
2 - splitar(separar) em uma nova variável (para que ela gere um vetor (lista)
3 - juntar as palavras  (passo anterior com esse servem para eliminar os espaços internos)
4 - criar uma varíavel vazia, para varrer a string de trás pra frente, gerando a string invertida no laço
5 - criar um laço, retornando o número de caracteres no string, para escrevê-la de trás pra frente,
    começando antes da última letra (- 1), indo até antes da primeira (-1),
    e vai voltando uma letra (-1) #ou simplesmente criar a inversão em uma variável usando fatiamento
6 - declarar o inverso
7 - verificar se o inverso e a junção são iguais com uma condicional simples
"""

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''  # é o equivalente a "variável = 0"
for letra in range(len(junto)-1, -1, -1):   #ou simplesmente criar a inversão em uma variável usando fatiamento (inverso = junto[::-1])
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')





