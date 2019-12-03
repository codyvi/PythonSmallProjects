import random
barajas=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
tableroNumeros=[]
tablero = [["-","-","-","-","-","-"], ["-","-","-","-","-","-"],["-","-","-","-","-","-"], ["-","-","-","-","-","-"], ["-","-","-","-","-","-"], ["-","-","-","-","-","-"]]
pares=[0,0]
ganador=[0]

def barajearCartas():
  random.shuffle(barajas)
  carta = 0
  for i in range(0, 6):
    fila = list()
    for j in range(0, 6):
      fila.append(barajas[carta])
      carta += 1
    tableroNumeros.append(fila)

def imprimirTablero():
  print("   0 1 2 3 4 5")
  for i in range(0, 6):
    print(i, end = "| ")
    for j in range(0, 6): 
      print(tablero[i][j], end=" ")
    print()

def estaDisponible(fila, columna):
  if (tablero[fila][columna] == "-"):
    return True
  return False

def imprimirMarcadores():
  print("El jugador 1 ha encontrado " + str(pares[0]) + " pares")
  print("El jugador 2 ha encontrado " + str(pares[1]) + " pares")

def primerPar():
  par = list()
  fila = -1
  columna = -1
  inputValido = False

  while(not inputValido):
    fila=int(input("De cual fila quieres voltear la primer carta? "))
    while(fila < 0 or fila > 5):
      print("Tienes que escoger un numero del 0 al 5, prueba de nuevo")
      fila=int(input("De cual fila quieres voltear la primer carta?  "))
    columna=int(input("De cual columna quieres voltear la primer carta? "))
    while(columna < 0 or columna > 5):
      print("Tienes que escoger un numero del 0 al 5, prueba de nuevo")
      columna=int(input("De cual columna quieres voltear la primer carta? "))

    if (estaDisponible(fila, columna)):
      tablero[fila][columna] = tableroNumeros[fila][columna]
      inputValido = True
    else:
      print("Esa carta ya esta volteada, prueba otra vez")
  par.append(fila)
  par.append(columna)
  # imprimirTablero()
  print("Tu primera carta es " + str(tablero[fila][columna]))
  return par

def segundoPar(primer):
  par = list()
  fila = -1
  columna = -1
  inputValido = False

  while(not inputValido):
    fila=int(input("De cual fila quieres voltear la segunda carta? "))
    while(fila < 0 or fila > 5):
      print("Tienes que escoger un numero del 0 al 5, prueba de nuevo")
      fila=int(input("De cual fila quieres voltear la segunda carta? "))
    columna=int(input("De cual columna quieres voltear la segunda carta? "))
    while(columna < 0 or columna > 5):
      print("Tienes que escoger un numero del 0 al 5, prueba de nuevo")
      columna=int(input("De cual columna quieres voltear la segunda carta? "))

    if (fila == primer[0] and columna == primer[1]):
      print("Esa habia sido tu primera carta, escoge otra")
    else: 
      if (estaDisponible(fila, columna)):
        tablero[fila][columna] = tableroNumeros[fila][columna]
        inputValido = True
      else:
        print("Esa carta ya esta volteada, prueba otra vez")
  par.append(fila)
  par.append(columna)
  # imprimirTablero()
  print("Tu segunda carta es " + str(tablero[fila][columna]))
  return par

def checarPar(par1, par2, jugador): 
  if (tablero[par1[0]][par1[1]] == tablero[par2[0]][par2[1]]):
    imprimirTablero()
    print("Encontraste el par de " + str(tablero[par1[0]][par1[1]]))
    if (jugador == 1):
      pares[0] += 1
    else:
      pares[1] += 1
  else:
    imprimirTablero() 
    print("No encontraste ningun par, se voltaran las cartas de nuevo")
    tablero[par1[0]][par1[1]] = "-"
    tablero[par2[0]][par2[1]] = "-"

def turnoJugadorUno():
  print("Es el turno del jugador 1")
  par1 = primerPar()
  par2 = segundoPar(par1)
  checarPar(par1, par2, 1)

def turnoJugadorDos():
  print("Es el turno del jugador 2")
  par1 = primerPar()
  par2 = segundoPar(par1)
  checarPar(par1, par2, 0)

def checarGanador():
  if (pares[0]+pares[1] == 18):
    if (pares[0] > pares[1]):
      print("El ganador ha sido el jugador 1 con " + str(pares[0]) + " pares")
    else:
      if (pares[0] == pares[1]):
        print ("Ambos jugadores han quedado empatados con " + str(pares[0]) + " pares")
      else: 
        print("El ganador ha sido el jugador 2 con " + str(pares[1]) + " pares")
    ganador[0] += 1
    return True
  return False
  
def juegoEnProgreso():
  imprimirTablero()
  imprimirMarcadores()
  if (not checarGanador()): 
    turnoJugadorUno()
    if (not checarGanador()):
      turnoJugadorDos()

def main():
  barajearCartas()
  seDeseaJugar = True
  while (seDeseaJugar and ganador[0] == 0):
    juegoEnProgreso()
    if (ganador[0] == 0):
      respuesta=input("¿Se desea seguir jugando? (Y/N) ")

      respuesta = respuesta.lower()
      if(respuesta == "n"):
        seDeseaJugar = False

main()