'''

Qual o valor de cada uma das expressões?

'''

print(3 == 3)       #T
print(3 != 3)       #F
print(3 >= 4)       #F
print(not (3 < 4))  #F

'''
Escreva uma função que, dada uma nota, retorna um string — o grau da nota de acordo com o esquema:

Nota

Grau

>= 90

A

[80-90)

B

[70-80)

C

[60-70)

D

< 60

F
'''

def GetGrau(nota):
    if (nota >= 90):
        ResultadoGrau = 'A'
    elif (nota >= 80) and (nota < 90):
        ResultadoGrau = 'B'
    elif (nota >= 70) and (nota < 80):
        ResultadoGrau = 'C'
    elif (nota >= 60) and (nota < 70):
        ResultadoGrau = 'D'
    else:
        ResultadoGrau = 'F'
    return ResultadoGrau

nota = input('Informe sua nota 0 - 100): ')
nota = nota.replace(',','.')
nota = float(nota)
print('''\n ► O grau de seu aproveitamento foi "''', GetGrau(nota), '''"\n''')

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for i in xs:
    print(GetGrau(i))

"""
6- Escreva uma função acheHipot que, dados os comprimento de dois lados de um triângulo retângulo,
retorna o comprimento da hipotenusa. (Dica: o valor de x ** 0.5 é a raiz quadrada, ou use sqrt do módulo matemático)
"""
def acheHipot(Lado1, Lado2):
    return round((Lado1 ** 2 + Lado2 ** 2) ** 0.5, 4)

Lado1, Lado2 = input('Informe o lado 1 do triângulo retângulo: '), input('Informe o lado 2 do triângulo retângulo: ')
Lado1 = float(Lado1.replace(',','.'))
Lado2 = float(Lado2.replace(',','.'))
print('Valor da hipotenusa deste triângulo retângulo é', acheHipot(Lado1, Lado2))

