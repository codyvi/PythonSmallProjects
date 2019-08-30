import qrcode 

data = "Nombre: "
data += input("¿Cual es tu nombre? \n ")
data += " Matrícula: "
data += input("Cuál es tu matricula? \n ")
qr = qrcode.make(data)
qr.save("myQR.jpg")