from tinydb import TinyDB, Query

db = TinyDB('./tmp/db.json')

table1 = db.table('Proyectos')
table1.insert({'ID' : 1 , 'Nombre' : 'Gravity', 'Encargado' : 'Victor', 'Presupuesto' : 80000})

table2 = db.table('Encargados')
table2.insert({'ID' : 1 , 'Nombre' : 'Victor' })

Name = Query()
yeet = table1.search(Name.Nombre == 'Gravity')
print(yeet)
