'''
Problema Prático 4.1
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões (usando s e o operador de indexação) que sejam avaliadas como:
(a)'234'
(b)'78'
(c)'1234567'
(d)'0123'
(e)'789'
'''

s = '0123456789'
print('\n' + str('>>> Problema Prático 4.1 - operador de indexação <<<').center(80,'-') )
print('(a) ', s[2:5])
print('(b) ', s[7:9])
print('(c) ', s[1:8])
print('(d) ', s[:4])
print('(e) ', s[7:])
