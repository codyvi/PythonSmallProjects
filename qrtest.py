import qrcode 

data = input("¿Cual es tu nombre? \n ")
data += input("Cuál es tu matricula? \n ")
qr = qrcode.make(data)
qr.save("myQR.jpg")