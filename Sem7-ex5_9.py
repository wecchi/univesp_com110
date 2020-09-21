'''
5.9 Usamos o padrão de laço aninhado para gerar todos os pares de índices de coluna e linha e somarmos as entradas correspondentes:

'''

def add2D(t1, t2):
    '''t1 e t2 são listas 2D com o mesmo número de linhas e
    mesmo número de colunas de tamanho igual
    add2D incrementa cada item t1[i][j[ por t2[i][j]'''
    nlinhas = len(t1)               # número de linhas
    ncolunas = len(t1[0])           # número de colunas
    for i in range(nlinhas):        # para cada índice de linha i
        for j in range(ncolunas):   # para cada índice de coluna j
            t1[i][j] += t2[i][j]

print('\n' + str('>>> Problema Prático 5.9 Usando padrão de laço aninhado <<<').center(80,'-') )

# Definindo uma lista 't1'
t1 = [[x**2 for x in range(10)] , [y+1 for y in range(10)], [z-10 for z in range(10)]]
print('t1 = ' , str(t1).rjust(120,'.') )

# Definindo uma lista 't2'
t2 = [[x//3 for x in range(20,120,10)] , [y-1 for y in range(10)], [z*5 for z in range(10)]]
print('t2 = ' , str(t2).rjust(120,'.') )

#Aplicando a função 'add2D'
add2D(t1, t2)
print('t1 + t2 =  ' , str(t1))
