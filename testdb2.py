from tinydb import TinyDB, Query

def Convert(string): 
    li = list(string.split(" ")) 
    return li 


db = TinyDB('./tmp/db.json')
Name = Query()
yeet = db.search(Name.name == 'david')


    
#Convierto a string la lista con un atributo
str1 = ''.join(str(e) for e in yeet)
# print(str1)
#conviero el string a lista pero ya separada y pues ya nada mas es de saber en que indice esta el atributo  
newli = Convert(str1)

s = newli[len(newli) - 1]
#le quito los '{' del json
s = s.translate({ord(i): None for i in '"}'})
s = s.translate({ord(i): None for i in "'"})

print(s)