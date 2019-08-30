#Ejercicios de Programación Funcional en Python 

#version tradicional
def suma(val1, val2): 
    return val1+val2

def operacion(funcion, val1,val2):
    return funcion(val1,val2)

def resta(val1, val2):
    return val1-val2

def cuadrado(elemento):
    return elemento*elemento

funcion_suma = suma
funcion_resta = resta

resultadosuma = operacion(funcion_suma, 10, 20)
resultadoresta = operacion(funcion_resta, 20, 10)

lista = [10,20,30]
resultadocuadrado = list(map(cuadrado, lista))
#print(resultadocuadrado)


#FUNCIONAL
sumaf = lambda val1, val2 : val1 + val2
restaf = lambda val1, val2 : val1-val2
operacionf = lambda operacion, val1, val2 : operacion(val1, val2)
#print(operacionf(restaf, 10, 20))
resultadof = list(map(lambda elemento : elemento * elemento, lista))
#print(resultadof)


listat = [1,2,3,4,5,6,7]
total = 0

for elemento in listat:
    total += elemento

#print(total)


from functools import reduce
listatt = [1,2,3,4,5,6,7]

def funcion_acumulador(acumulador, elemento):
    return acumulador + elemento

#print(reduce(funcion_acumulador, listatt))


listaa = ['Python', 'Java', 'C', 'C++']
resulado = reduce(lambda acumulador, elemento : acumulador + ' * ' + elemento, listaa)
#print(resulado)

letters = list(map(lambda x : x, 'humano'))
print(letters)

matrix = [[1,2,3,4],[4,5,6,8]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)