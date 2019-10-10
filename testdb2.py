from tinydb import TinyDB, Query



db = TinyDB('db.json')
Cars = Query()
yeet = db.search(Cars.color == 'green')

print(yeet)