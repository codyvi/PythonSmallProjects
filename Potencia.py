# A00822455
# David Alonso Cantú Martínez
# Funcion Potencia
def SetPot(SetP):
    if(len(SetP) == 0):
        return [[]]
    #Llamada recursiva para obtener la función potencia
    r = SetPot(SetP[:-1])
    return r + [s + [SetP[-1]] for s in r]

#Función para ordenar los valores de la función potencia del vació al mayor.
def Ordenar(SetP):
    for e in sorted(SetP, key=lambda s: (len(s), s)):
        print(e)

Ordenar(SetPot([1,2,3,4,5,6,7,8,9]))
