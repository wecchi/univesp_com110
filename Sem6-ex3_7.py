'''
Problema Prático 3.7
Escreva um laço for que exiba a seguinte sequência de números, um por linha.
(a)Inteiros de 3 até 12, inclusive este.
(b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
(c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
(d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.
'''

print('\n' + str('>>> Problema Prático 3.7 imprimindo inteiros <<<').center(80,'-') )

# (a)Inteiros de 3 até 12
print('(a)Inteiros de 3 até 12')
for n in range(3,13):
    print(n)

# (b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1
print('\n(b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1')
for n in range(0,9,2):
    print(n)

# (c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
print('\n(c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.')
for n in range(0,24,3):
    print(n)

# (d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.
print('\n(d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.')
for n in range(3,12,5):
    print(n)
