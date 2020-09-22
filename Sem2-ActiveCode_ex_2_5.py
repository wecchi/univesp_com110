'''
Considere a sentença:
Só trabalho sem diversão faz de João um chato.

Armazene cada palavra em uma variável, então imprima a sentença uma palavra por linha usando a função print.

'''

frase = 'Só trabalho sem diversão faz de João um chato'
palavras = frase.split(' ')

print('''A frase a ser impressa será "''', frase, '''"''', '\n')

for palavra in palavras:
    print(palavra, '\n')


