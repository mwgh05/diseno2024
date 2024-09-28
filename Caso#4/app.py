from flask import Flask, jsonify, request
from pymongo import MongoClient
import random
from bson import json_util  

app = Flask(__name__)


client = MongoClient("mongodb://mongodb:27017/")
db = client.registros
collection = db.datos

client_pool = MongoClient("mongodb://mongodb:27017/", maxPoolSize=10)
db_pool = client_pool.registros
collection_pool = db_pool.datos


@app.route("/")
def ruta_base():
    return "{\"message\":\"Se permite la conexión\"}"

@app.route('/get_registros', methods=['GET'])
def get_registros():
    total = list(collection.find())
    total_count = len(total)
    percentage_35 = int(total_count * 0.35)
    resultado = random.sample(total, percentage_35)

    response = {
        "total_registros": total_count,
        "registros_devueltos": len(resultado),
        "data": resultado
    }

    return json_util.dumps(response), 200

@app.route('/get_registros_poolsize', methods=['GET'])
def get_registros_poolsize():
    total = list(collection_pool.find())
    total_count = len(total)
    percentage_35 = int(total_count * 0.35)
    resultado = random.sample(total, percentage_35)

    response = {
        "total_registros": total_count,
        "registros_devueltos": len(resultado),
        "data": resultado
    }

    return json_util.dumps(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
