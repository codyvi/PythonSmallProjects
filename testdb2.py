from tinydb import TinyDB, Query
import json

def Convert(string): 
    li = list(string.split(" ")) 
    return li 


db = TinyDB('db.json')
Cars = Query()
yeet = db.search(Cars.color == 'green')


    
#Convierto a string la lista con un atributo
str1 = ''.join(str(e) for e in yeet)
print(str1)
#conviero el string a lista pero ya separada y pues ya nada mas es de saber en que indice esta el atributo  
newli = Convert(str1)

s = newli[len(newli) - 1]
#le quito los '{' del json
s = s.translate({ord(i): None for i in '"}'})

print(s)