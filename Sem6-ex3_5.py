'''
3.5 Implemente um programa que solicite do usuário uma lista de palavras e depois imprime na tela apenas as que strings de 4 letras:

'''

print('\n' + str('>>> Problema Prático 3.5 trabalhando com strings <<<').center(80,'-') )

# Obtendo um texto do usuário 'frase'
frase = input('Informe palavras para serem avaliadas: ')

# Definindo uma lista com as palavras 'palavras'
palavras = frase.split(' ')

print('\nPalavras com 4 letras:')
#Efetuando um laço para vefificar o tamanho das palavras
for palavra in palavras:
    if len(palavra) == 4:
        print('...  ', str(palavra).upper())
