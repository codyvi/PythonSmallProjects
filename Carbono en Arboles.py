import math

DensidadArbol = float(input('Dame la densidad del arbol en kilogramos: '))
AlturaArbol = float(input('Dame la altura del arbol en metros: '))
DiametroArbol = float(input('Dame el diametro del arbol en metros: '))


# s = 450.88 + 464.48 + 536.46 + 494.13 + 406.32 + 958.36 + 1147.43 + 840.29 + 219.41 + 275.99 + 134.62 + 395.82 + 395.82 + 579.96 + 717.82 + 584.79 + 480.76 + 216.93 + 210.84 + 292.58
# print (s) 

# n = s *.49
# print (n)

g = math.pi/4 * math.pow(DiametroArbol, 2)

V = g * AlturaArbol * .6

B = V * DensidadArbol * 1.35

C = B *.49

print ('G =', +g)
print ('V =', +V)
print ('B =', +B)
print ('El Carbono en el arbol es', +C, 'kg')
