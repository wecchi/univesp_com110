'''
No caso de duas dimensões, podemos criar
uma lista de listas:

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Corresponde a uma matriz 3 x 3:
1 2 3
4 5 6
7 8 9


Assim, m[0] corresponde à primeira linha
(lista [1, 2, 3]), m[1] à segunda linha (lista [4,
5, 6]) e m[2] à terceira linha (lista [7, 8, 9]).

'''


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m[0] implica em acessar [1, 2, 3]
# m[0][0] implica em acessar o elemento ZERO da lista zero
m[0][0] == 1

#implementar uma função que verifica se a matriz é simétrica (matriz == a matriz transposta)
def simetrica(m):
    nlinhas = len(m)
    ncolunas = len(m[0])

    for i in range(nlinhas):
        for j in range(ncolunas):
            if m[i][j] != m[j][i]:
                return False
    return True

print('\n' + str(' Versão 1 - Verificando simetria da matriz ').center(80,'-') )
if simetrica(m):
    print('''\nA matriz "%s" é simétrica, ou seja a sua transposta possui os mesmo elementos posicionais'''%m)
else:
    print('''\nA matriz "%s" não é simétrica, ou seja a sua transposta possui elementos diferentes ao posicionais'''%m)


print('\n' + str(' Versão 2 - Verificando simetria da matriz ').center(80,'-') )
m = [[1, 2, 3], [2, 4, 5], [3, 5, 3]]
if simetrica(m):
    print('''\nA matriz "%s" é simétrica, ou seja a sua transposta possui os mesmos elementos posicionais'''%m)
else:
    print('''\nA matriz "%s" não é simétrica, ou seja a sua transposta possui elementos diferentes ao posicionais'''%m)


'''
Implementar uma função em Python que
recebe uma matriz bidimensional e retorna
sua correspondente transposta.
'''

print('\n' + str(' Versão 3 - Criando matriz transposta ').center(80,'-') )
matrix = [[1,-5,2,0],[3,0,4,12],[5,6,8,7],[7,8,9,-4]]
transposta = [[linha[coluna] for linha in matrix] for coluna in range(len(matrix[0]))]
print(transposta)
            
    
