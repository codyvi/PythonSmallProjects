def Convert(string): 
    li = list(string.split(" ")) 
    return li 

word = '{"main": "Nombre: David Alonso Cantu Martinez  Matricula: A00822455"}'


newWord = Convert(word)

size = len(newWord)-1

# if newWord[size] 

print(newWord[8])