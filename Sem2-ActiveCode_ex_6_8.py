"""

Escreva uma função chamada é_impar(n) que recebe como argumento um inteiro e retorna True se o argumento é um número ímpar e False se ele é par.

"""
def é_impar(n):
    return (n % 2) != 0

Numero = input('Informe um número: ')
Numero = float(Numero.replace(',','.'))

print('O número é ímpar?', é_impar(Numero))

