from pymongo import MongoClient

def insert_dati(dato):

    client = MongoClient('mongodb://localhost:27017')
    db = client['db-progetto']
    collezione = db.sensori
    collezione.insert_one(dato)
