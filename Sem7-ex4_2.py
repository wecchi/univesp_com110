'''
Problema Prático 4.2
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:
(a)À variável cont, a quantidade de ocorrências da string 'day' na string previsão.
(b)À variável clima, o índice em que a substring 'sunny' começa.
(c)À variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'.


--------------------------------------------------------------------------------------------------

Uso             Valor Retornado
s.capitalize()	Uma cópia da string s com o primeiro caractere em maiúscula, se for uma letra no alfabeto
s.count(alvo)	O número de ocorrências da substring alvo na string s
s.find(alvo)	O índice da primeira ocorrência da substring alvo na string s
s.lower()	Uma cópia da string s convertida para minúsculas
s.replace(antiga, nova)	Uma cópia da string s em que cada ocorrência antiga, quando a string s é lida da esquerda para a direita, é substituída pela substring nova
s.translate(tabela)	Uma cópia da string s na qual os caracteres foram substituídos usando o mapeamento descrito pela tabela
s.split(sep)	Uma lista de substrings strings s, obtida usando a string delimitadora sep; o delimitador padrão é o espaço em branco
s.strip()	Uma cópia da string s sem espaços no início e no final
s.upper()	Uma cópia da string s convertida para maiúsculas


'''

previsão = 'It will be a sunny day today'
print('\n' + str('>>> Problema Prático 4.2 - métodos de string <<<').center(80,'-') )

cont = previsão.count('day')
print('(a) cont=%d'%cont)

clima = previsão.find('sunny')
print('(b) clima =%d'%clima)

troca = previsão.replace('sunny', 'cloudy')
print('''(c) troca = "%s"'''%troca)
