m = int(input("Dame un número de registros: "))



f= open("test.txt","w+")

for i in range(m):
     f.write("Registro %d\r\n" % (i+1))

f.close() 

