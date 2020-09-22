'''

Conceitos e aplicações – uma abordagem didática (Ler: seções 2.3, 2.4 e 4.1) | Sérgio Luiz Banin

Atribuição múltipla de variáveis
Atribuição posicional de variáveis
identificador da variável id()


'''

A = B = C = 34
print('A = B = C = 34 id(A)', id(A) == id(B), id(C))
D, E, F = 500, 600, 700
print('\n', D, E, F)

# Usando atribuição incremental de variável
print('\n A = ',A)
A += 56
print('A += 56  ...  ',A)
A -= 8
print('A -= 8  ...  ',A)
A *=152
print('A *=152  ...  ',A)
A **=3
print('A **=3  ...  ',A)
A /=6
print('A /=6  ...  ',A)
A //=3
print('A //=3  ...  ',A)
A %=5
print('A %=5  ...  ',A)

from math import sqrt
y = 81
print('\n', y, sqrt(y))
