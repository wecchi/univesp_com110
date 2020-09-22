'''
Texto de apoio - Python3 – Conceitos e aplicações – uma abordagem didática (Ler: seções 2.3, 2.4 e 4.1) | Sérgio Luiz Banin

Problema Prático 2.1
Escreva expressões algébricas Python correspondentes aos seguintes comandos:
(a)A soma dos 5 primeiros inteiros positivos.
(b)A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
(c)O número de vezes que 73 cabe em 403.
(d)O resto de quando 403 é dividido por 73.
(e)2 à 10a potência.
(f)O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
(g)O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
'''
a = 1 + 2 + 3 + 4 + 5
b = (23 + 19 + 31) / 3
c = 403 // 73
d = 403 % 73
e = 2 ** 10
f = abs(54 - 57)
g = min(34.99, 29.95, 31,50)

print('(a)A soma dos 5 primeiros inteiros positivos.', a)
print('(b)A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).', b)
print('(c)O número de vezes que 73 cabe em 403.', c)
print('(d)O resto de quando 403 é dividido por 73.', d)
print('(e)2 à 10a potência.', e)
print('(f)O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).', f)
print('(g)O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50. ', g)
