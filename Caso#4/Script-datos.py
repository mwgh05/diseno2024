from pymongo import MongoClient
from faker import Faker

client = MongoClient("mongodb://localhost:27017/")
db = client.registros
collection = db.datos




fake = Faker()
lista_registros = []

for _ in range(60000):
    lista_registros.append({
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "age": fake.random_int(min=18, max=80)
    })

collection.insert_many(lista_registros)



total = list(collection.find())