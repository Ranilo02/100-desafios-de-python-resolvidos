"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar para cada palavra quais são suas vogais.
"""

palavras = ('RANILO', 'PROGRAMADOR', 'NOTEBOOK', 'COMPUTADOR', 'GABINETE', 'FILOSOFIA', 'SOFTWARE',)
for p in palavras:   # p é o contador de elementos da lista 'palavras', isto é, cada palavra
    print(f'\nNa palavra {p} temos ', end=' ')
    for letra in p:  # letra é o contador/selecionador de elementos(no caso as letras) da lista(no caso, cada palavra é uma lista) lê-se: para cada letra in p
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
