def producto(): 
    n = 1
    k = 3
    contador = 0
    Pf = 1
    for contador in range(n, k+1):
        producto = contador *contador
        Pf *= producto
        print (Pf)
    return Pf

def Suma1():
    n = 1
    k = 4
    contador = 0
    ProdF = 0
    for contador in range(n, k+1):
        Suma = contador*(1+contador)
        ProdF += Suma
        print(ProdF)
    return ProdF 

def Suma2():
    n = -1
    k = 0
    contador = 0
    ProdF = 0
    for contador in range(n, k+1):
        Suma = (2**contador)*(3+contador)
        ProdF += Suma
        print(ProdF)
    return ProdF 


print('Producto')
var1 = producto()
varStr = str(var1)
print('El valor del producto de 1 a 3 es: ' +varStr)
print('Suma 1')
var2 = Suma1()
var2str = str(var2)
print('El valor de la sumatoria 1 de 1 a 4 es: ' +var2str)
print('Suma 2')
var3 = Suma2()
var3str = str(var3)
print('El valor de la sumatoria 2 de -1 a 0 es: ' +var3str)