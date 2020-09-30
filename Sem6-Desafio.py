'''
Desafio Semana 6
Como você implementaria um programa que precisasse calcular a média de 1 milhão de valores?
'''

print('\n' + str('>>> Desafio Semana 6 - média 1 de milhão de valores <<<').center(80,'-') )

import numpy as np
notas = np.random.randint(1,10, size = 10**6)
print('Média', round(np.mean(notas),2))
print('Desvio padrão', round(np.std(notas),2))
