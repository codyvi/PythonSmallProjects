def Convert(string): 
    li = list(string.split(" ")) 
    return li 

word = '{"main": "Nombre: David Alonso Cantu Martinez  Matricula: A00822455"}'
wor2 = '{"id": 1, "name: car1, color: green"}'


newWord = Convert(word)

size = len(newWord)-1

s = newWord[size]

s = s.translate({ord(i): None for i in '"}'})


print(s)