"""

Escreva uma função é_ânguloreto que, dado o comprimento de três lados de um triângulo, determina se o triângulo é retângulo.
Asssuma que o terceiro argumento é sempre o lado maior. Ela retorna True se é um triângulo retângulo, ou False caso contrário.

Dica: aritimética de ponto flutuante não é sempre exatamente precisa, de forma que não é seguro testar números em ponto flutuante para igualdade.
Se um bom programador deseja saber se x é igual ou suficientemente perto de y, ele provavelmente usaria em seu código if  abs(x-y) < 0.0001:      # se x é aproximadamente igual a  y
Estenda o programa acima de forma que os lados possam ser dados à função em qualquer ordem.

"""
def é_triangulo_retangulo(Lado1, Lado2, Lado3):
    Lado1 = float(Lado1.replace(',','.'))
    Lado2 = float(Lado2.replace(',','.'))
    Lado3 = float(Lado3.replace(',','.'))
    Lados = [Lado1, Lado2, Lado3]
    Hipotenuza = max(Lados)
    CatetoAdjacente = min(Lados)
    if (Lado1 != Hipotenuza) and (Lado1 != CatetoAdjacente):
        CatetoOposto = Lado1
    elif (Lado2 != Hipotenuza) and (Lado2 != CatetoAdjacente):
        CatetoOposto = Lado2
    else:
        CatetoOposto = Lado3
        
    print('► Hipotenuza', Hipotenuza)
    print('► CatetoOposto', CatetoOposto)
    print('► CatetoAdjacente', CatetoAdjacente)

    Diferenca = CatetoOposto ** 2 + CatetoAdjacente ** 2 - Hipotenuza ** 2
    print('► Diferenca Teorema de Pitagoras', Diferenca)
    return abs(Diferenca) < 0.0001

L1, L2, L3 = input('Informe os lados do seu triângulo : '), input('Informe os lados do seu triângulo : '), input('Informe os lados do seu triângulo : ')
print('\n ►►► Seu triângulo é retângulo?', é_triangulo_retangulo(L1, L2, L3))

