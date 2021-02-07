Numeros = [3.6, 8.9, 10]
FatorAmortizador = 4
N = len(Numeros)
D = 0
for n in Numeros:
    D += 1 / (n + FatorAmortizador)
H = N / D - FatorAmortizador
print(H)
