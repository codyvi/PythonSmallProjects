def InteresSimple(C, i, n):
  I = C*i*n
  return (I)

Nombre = input("Dame tu nombre: ")
Capital = int(input("Dame tu Capital: "))
InteresA = float(input("Dame tu Interes: "))
NumeroDeA = int(input("Dame tu Numero de Años: "))

Cstr = str(Capital)
IntStr = str(InteresA)
Numstr = str(NumeroDeA)

InteresS = InteresSimple(Capital, InteresA, NumeroDeA)

IntSstr = str(InteresS)

print('Estimado ' +Nombre, 'tu capital de ' +Cstr, 'invertido con un interes anual ' +IntStr, 'en ' +Numstr, 'años te dio ' +IntSstr, 'de dinero')