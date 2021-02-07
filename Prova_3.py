
'''
Implemente uma função em Python que receba uma string como parâmetro e imprima as vogais
dessa string. Exemplo: string ‘univesp’ → deve imprimir os caracteres ‘u’, ‘i’ e ‘e’.
'''
def ImprimeVogal (texto):
    print('\n>> Vogais encontradas' )
    for i in texto:
        if i in ('a', 'e', 'i', 'o,', 'u', 'A', 'E' ,'I', 'O', 'U'):
            print (i)

print('\n' + str('>>> Impressão das vogais <<<').center(80,'-') )
frase = input('Digite uma frase: ')
ImprimeVogal(frase)

