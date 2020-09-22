'''
Escreva um programa que calcula a área de um retângulo.
O programa deve pedir ao usuário que entre com a altura e a largura do retângulo.
Em seguida deve imprimir uma mensagem com a resposta.
'''

l, h = input('Entre com a Largura do retângulo: '), input('Entre com a Altura do retângulo: ')
l = l.replace(',','.')
h = h.replace(',','.')

print('Área do retângulo:', round(float(l)*float(h),2))
