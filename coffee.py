from pymongo import MongoClient
from Grain import Grain 


def grains_valid():
    client = MongoClient(host='mongodb')
    db = client["ma_base"]
    col = db["ma_collection"]

    for i in col.find():
        grain = Grain(i["origine"], i["arome"], i["année"], i["corps"])
        if not grain.is_valid():
            print(f"Données de grain non valides : {i}")


if __name__ == "__main__":
    grains_valid()