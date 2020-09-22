'''
A fórmula para calcular o valor final de juros compostos (compound interest) é mostrada na Wikipedia como

A = P(1+r/n)**(nt)
Escreva um programa em Python que atribui o valor 10000 para a variável P `,
atribui para `n`o valor 12 e atribui para `r a taxa de juros de 8% (0.08).
O programa deve pedir ao usuário o número t de anos. Calcule e imprima o valor final depois de t anos

'''

P = 10000
n = 12
r = 0.08

t = input('Informe o número de anos para cálculo dos juros compostos: ')
t = t.replace(',','.')
t = int(t)

A = P*(1+r/n)**(n*t)

print('Valor final dos juros:', round(A,2))
