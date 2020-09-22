'''
Escreva um programa que calcula o consumo de gasolina de uma carro em quilômetros por litro.
O programa deve pedir ao usuário que entre com o número de quilômetros percorridos e o
número de litros de gasolina consumidos. Em seguida o programa deve imprimir a resposta.
'''

kmPercorridos = input('Quantos km foram percorridos? ')
kmPercorridos = int(kmPercorridos)
lGasolina = input('Quantos litros de gasolina foram abastecidos? ')
lGasolina = float(lGasolina)
Consumo = round(kmPercorridos / lGasolina,2)
print('Autonomia de ', Consumo, 'km/l')
