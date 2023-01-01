"""
Crie um programa em que o usuário possa digitar cinco valores númericos e cadastrá-los em uma lista.
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:  # ou lista[-1]  lê-se: se for o primeiro valor ou for maior que o último valor:
        lista.append(n)                    #acrescentar o valor do input n na lista
        print('Adicionado ao final da lista...')
    else:   # caso contrário,
        pos = 0
        while pos < len(lista):         #será feita uma varredura no vetor inteiro
            if n <= lista[pos]:         #verificar se o número que você quer inserir (n) é menor ou igual ao número na posição pos, isto é ele mesmo
                lista.insert(pos, n)    #e em caso positivo, inserí-lo na posição pos
                print(f'Adicionado na posição {pos} da lista...')
                break                   # como isso só será uma vez por número adicionado, 'break' para sair
            pos += 1                    # para ir passando para a próxima posição do vetor
print(f'Os valores digitados em ordem foram {lista}')


# forma alternativa muito mais simples, que vi em um comentário do video do exercicio 82 (Mateus Alves)

nuns = []
nuns_org = []

for x1 in range(0, 5):
    valor = int(input(f'> digite o {x1}° valor: '))
    nuns.append(valor)

for x2 in range(0, 5):
    menor = min(nuns)
    nuns_org.insert(x2, menor)
    nuns.remove(menor)

print(f'\n> numeros de forma organizada: {nuns_org}')