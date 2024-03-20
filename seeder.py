import pymongo
from pymongo import MongoClient

client = MongoClient(host="mongodb")

db = client["ma_base"]


col = db["ma_collection"]

donnees_valides = [
    {"origine": "Vietname", "arome": "Chocolate", "annee": 2021, "corps": 4 },
    {"origine": "Colombie", "arome": "Chocolate", "annee": 2021, "corps": 3}
]

donnees_invalides = [
    {"origine": "France", "arome": "Fraise", "annee": 2000, "corps": 10}
]

for i in donnees_valides:
    col.insert_one(i)

for i in donnees_invalides:
    try:
        col.insert_one(i)
    except Exception as e:
        print(f"Erreur lors de l'insertion de l'entrée non valide : {e}")

print("Peuplement de la base de données terminé.")