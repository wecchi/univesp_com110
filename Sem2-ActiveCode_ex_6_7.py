"""

Escreva uma função chamada é_par(n) que recebe como argumento um inteiro e retorna True se o argumento é um número par e False se ele é ímpar.

"""
def é_par(n):
    return (n % 2) == 0

Numero = input('Informe um número: ')
Numero = float(Numero.replace(',',''))

print('O número é par?', é_par(Numero))

