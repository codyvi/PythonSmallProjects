from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'id': 1, 'name': 'david', 'dinero': '8000'})
db.insert({'id': 2, 'name': 'carlos', 'dinero': '5000'})
db.insert({'id': 3, 'name': 'turriza', 'dinero': '0'})

