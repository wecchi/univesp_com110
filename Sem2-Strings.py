# Videoaula 7 - Strings
nome = input('Digite o seu nome completo: ')
nome2 = input('Qual o nome da sua mãe? ')
nome = nome.strip()
nome2 = nome2.strip()
print('é Marcelo? ', 'Marcelo' in nome)
print('Seu nome e de sua mãe são diferentes? ', nome != nome2)
print('Seu nome vem depois da sua mãe? ', nome > nome2)
print('Quantidade de letras do seu nome: ', len(nome))
print(nome.upper())

