def potencia(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*potencia(base,exp-1))
    
var1 = 0 
var2 = 2
var3 = 16
print('potencia',potencia(var2,var3))
var1 = (var3-1)
print('multiplicaciones',var1)

#se hacen n-1 multiplicaciones porque si empezamos en 1, se hacen 0 multiplicaciones, 
#entonces, siguiendo el código podemos ver que se hacen n = var3, -1 multiplicaciones

import math

def potencia_mejorada(base,exp):
    if(exp==1):
        return(base)
    if (exp % 2 == 0) :
        mult+=1
        return(potencia_mejorada(base*base,exp//2 ))
    if(exp!=1):
        mult+=2
        return(base*potencia_mejorada(base*base,(exp-1)//2))
var1 = 0
var2 = 2
var3 = 16
print('potencia', potencia(var2,var3))
var1 = 2* math.log2(4)
print('multiplicaciones',var1)

#Al momento de expandir la formula recursiva nos damos cuenta que se realizan log2(n) veces la multiplicación de adentro, luego hay otra multiplicación
#y por esta se vuelve 2log2(n)
