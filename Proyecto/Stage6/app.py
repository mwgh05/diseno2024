from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'Prueba',
    'host': 'mongodb',
    'port': 27017
}

db = MongoEngine(app)

# Definir los modelos
class Alert(db.Document):
    id = db.StringField(required=True, unique=True)
    experiment_id = db.StringField(required=True)
    type = db.StringField(required=True)
    description = db.StringField(required=True)
    date = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "id": self.id,
            "experiment_id": self.experiment_id,
            "type": self.type,
            "description": self.description,
            "date": self.date
        }

class Experiment(db.Document):
    id = db.StringField(required=True, unique=True)
    user_id = db.StringField(required=True)
    name = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.utcnow)
    steps = db.ListField(db.StringField(), default=list)
    alerts = db.ListField(db.StringField(), default=list)
    materials = db.ListField(db.StringField(), default=list)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "date": self.date,
            "steps": self.steps,
            "alerts": self.alerts,
            "materials": self.materials
        }

class Log(db.Document):
    id = db.StringField(required=True, unique=True)
    experiment_id = db.StringField(required=True)
    user_id = db.StringField(required=True)
    date_start = db.DateTimeField(default=datetime.utcnow)
    date_final = db.DateTimeField()
    detail = db.StringField()
    steps_completed = db.ListField(db.StringField(), default=list)
    materials_used = db.ListField(db.StringField(), default=list)

    def to_json(self):
        return {
            "id": self.id,
            "experiment_id": self.experiment_id,
            "user_id": self.user_id,
            "date_start": self.date_start,
            "date_final": self.date_final,
            "detail": self.detail,
            "steps_completed": self.steps_completed,
            "materials_used": self.materials_used
        }

class Material(db.Document):
    id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Organization(db.Document):
    id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    users = db.ListField(db.StringField(), default=list)
    address = db.StringField(required=True)
    contact = db.StringField(required=True)
    creationDate = db.DateTimeField(default=datetime.utcnow)
    updateDate = db.DateTimeField(default=datetime.utcnow)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users,
            "address": self.address,
            "contact": self.contact,
            "creationDate": self.creationDate,
            "updateDate": self.updateDate
        }

class Step(db.Document):
    id = db.StringField(required=True, unique=True)
    experiment_id = db.StringField(required=True)
    title = db.StringField(required=True)
    description = db.StringField(required=True)

    def to_json(self):
        return {
            "id": self.id,
            "experiment_id": self.experiment_id,
            "title": self.title,
            "description": self.description
        }

class User(db.Document):
    id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    organization = db.StringField(required=True)
    email = db.StringField(required=True)
    creationDate = db.DateTimeField(default=datetime.utcnow)
    updateDate = db.DateTimeField(default=datetime.utcnow)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "organization": self.organization,
            "email": self.email,
            "creationDate": self.creationDate,
            "updateDate": self.updateDate
        }

# endpoint GET dinámico
@app.route('/<collection_name>', methods=['GET'])
def get_collection(collection_name):
    collections = {
        'alerts': Alert,
        'experiments': Experiment,
        'logs': Log,
        'materials': Material,
        'organizations': Organization,
        'steps': Step,
        'users': User
    }

    collection = collections.get(collection_name)
    if not collection:
        return jsonify({"error": "Collection not found"}), 404

    documents = collection.objects()
    return jsonify([doc.to_json() for doc in documents])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)