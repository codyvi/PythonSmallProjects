import math

DensidadArbol = float(input('Dame la densidad del arbol en metros: '))
AlturaArbol = float(input('Dame la altura del arbol en metros: '))
DiametroArbol = float(input('Dame el diametro del arbol en metros: '))


g = math.pi/4 * math.pow(DiametroArbol, 2)

V = g * AlturaArbol * .6

B = V * DensidadArbol * 1.35

C = B *.49

print ('G =', +g)
print ('V =', +V)
print ('B =', +B)
print ('El Carbono en el arbol es', +C, 'kg')

