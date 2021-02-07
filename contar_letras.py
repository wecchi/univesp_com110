def countLetter(textAsCount, l):
    x = textAsCount.count(l)
    return x

frase = input('digite uma frase qualquer ')
letra = input('que letra deseja contar? ')
print('\n','''Encontramos %d letras "%s"s no seu texto "%s"'''%(countLetter(frase, letra), letra, frase[:8] + '...'))
