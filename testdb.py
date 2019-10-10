from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'id': 1, 'name': 'car1', 'color': 'green'})
db.insert({'id': 2, 'name': 'car2', 'color': 'red'})
db.insert({'id': 3, 'name': 'car3', 'color': 'blue'})
