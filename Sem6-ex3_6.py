'''
Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.
(a)Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
(b)Inteiros de 0 a 1 (isto é, 0, 1).


'''

print('\n' + str('>>> Problema Prático 3.6 imprimindo inteiros <<<').center(80,'-') )

# (a)Inteiros de 0 a 9
print('(a)Inteiros de 0 a 9')
for n in range(0,10):
    print(n)

# (b)Inteiros de 0 a 1
print('\n(b)Inteiros de 0 a 1')
for n in range(0,2):
    print(n)
