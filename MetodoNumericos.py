import random as u

def genAleatorios():
    arr = []
    for _ in range(100):
        U = u.uniform(0.0,1.0) #Generando U entre 0 y 1 
        #Checo los valores de probabilidades para asignar a X
        if(U < 0.3):
            X = 1
        elif(U < 0.5):
            X = 2
        elif(U < 0.6):
            X = 3
        else:
            X = 4
        #Guardo los valores en la lista
        arr.append(X)
    return arr

#Función usada para contar las frecuencias de los datos 
def count_frequencies(data, relative = False):
    counter = {}
    for element in data:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1
    if relative:
        for element in counter:
            counter[element] /= len(data)
    return counter

#Imprimo la frecuencia de los datos en forma de porcentaje
print('Frecuencia de los datos:',count_frequencies(genAleatorios(), relative= True))
#Imprimo los valores en orden ascendente del 1 al 4
val = genAleatorios()
val.sort()
print(val)