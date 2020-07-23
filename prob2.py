def mayorDiferencia(x):
    valorMax = max(x)
    valorMin = min(x[:valorMax])

    return valorMax - valorMin




print(mayorDiferencia( [ 1, 1, 4 ]))
print(mayorDiferencia( [ 9, 8 ]))
print(mayorDiferencia( [ 6, 22, 16, 29, 23 ]))
print(mayorDiferencia( [ 28, 16, 28, 11, 14, 26, 23, 25, 17, 3, 22, 23, 23, 10 ]))