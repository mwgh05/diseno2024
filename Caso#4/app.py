from flask import Flask, jsonify, request
from pymongo import MongoClient
import random
from bson import json_util 
import redis 

app = Flask(__name__)


client = MongoClient("mongodb://mongodb:27017/")
db = client.registros
collection = db.datos

client_pool = MongoClient("mongodb://mongodb:27017/", maxPoolSize=10)
db_pool = client_pool.registros
collection_pool = db_pool.datos

# Redis Client
redis_cliente = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

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

@app.route('/get_registros_cache', methods=['GET'])
def get_registros_cache():
    
    # Verificar si los datos estan en la cache
    cached_data = redis_cliente.get('registros_cache')
    if cached_data:
        return json_util.dumps({"data": json_util.loads(cached_data), "source": "cache"}), 200
    
    # Traer de base de datos
    total = list(collection_pool.find())
    total_count = len(total)
    
    # En caso de no encontrar nada devolver 0 registros y no guardar en cache
    if total_count == 0:
        return json_util.dumps({"data": {"total_registros": 0, "registros_devueltos": 0, "data": []}, "source": "database"}), 200
    
    percentage_35 = int(total_count * 0.35)
    resultado = random.sample(total, percentage_35)
    
    response = {
        "total_registros": total_count,
        "registros_devueltos": len(resultado),
        "data": resultado
    }
    
    # Poner el resultado en cache
    redis_cliente.set('registros_cache', json_util.dumps(response), ex=60)
    
    return json_util.dumps(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
