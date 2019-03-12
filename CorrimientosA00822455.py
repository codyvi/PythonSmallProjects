corrimiento = 4

inicio = -3
limite = 9
sumatoria = 0
terminos_sumados_corrimiento = []

for contador in range (inicio + corrimiento, limite+1 + corrimiento) :
    print(contador,' ', end='') 
    sumatoria = 9+7* contador 
    sumatoria_sin_corrimiento = 9+7 *(contador - corrimiento)
    print('con corrimiento :', sumatoria, 'sin corrimiento :',sumatoria_sin_corrimiento,'=',\
           7*contador,'-',7*corrimiento,'+', 37, '--->' , '7 *',contador , 37-7*corrimiento)
    
