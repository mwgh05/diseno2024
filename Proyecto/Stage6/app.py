from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from datetime import datetime
import logging

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'Prueba',
    'host': 'mongodb://mongodb:27017/',
    'port': 27017
}

db = MongoEngine(app)

class Step(db.Document):
    id = db.StringField(primary_key=True)
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

class Alert(db.Document):
    id = db.StringField(primary_key=True)
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

class Material(db.Document):
    id = db.StringField(primary_key=True)
    name = db.StringField(required=True)
    description = db.StringField(required=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Experiment(db.Document):
    id = db.StringField(primary_key=True)
    user_id = db.StringField(required=True)
    name = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.now())
    steps = db.ListField(db.ReferenceField('Step', reverse_delete_rule=db.PULL), default=list)
    alerts = db.ListField(db.ReferenceField('Alert', reverse_delete_rule=db.PULL), default=list)
    materials = db.ListField(db.ReferenceField('Material', reverse_delete_rule=db.PULL), default=list)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "date": self.date,
            "steps": [step.to_json() for step in self.steps],
            "alerts": [alert.to_json() for alert in self.alerts],
            "materials": [material.to_json() for material in self.materials]
        }

class Log(db.Document):
    id = db.StringField(primary_key=True)
    experiment_id = db.StringField(required=True)
    user_id = db.StringField(required=True)
    date_start = db.DateTimeField(default=datetime.utcnow)
    date_final = db.DateTimeField()
    steps_completed = db.ListField(db.StringField(), default=list)
    materials_used = db.ListField(db.StringField(), default=list)

    def to_json(self):
        return {
            "id": self.id,
            "experiment_id": self.experiment_id,
            "user_id": self.user_id,
            "date_start": self.date_start,
            "date_final": self.date_final,
            "steps_completed": self.steps_completed,
            "materials_used": self.materials_used
        }

class Organization(db.Document):
    id = db.StringField(primary_key=True)
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

class User(db.Document):
    id = db.StringField(primary_key=True)
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

# Endpoint to insert provided data
@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        alerts = [
            {"id": "alert_001", "experiment_id": "exp_001", "type": "informativa", "description": "Descripción de la alerta 1", "date": datetime.now()},
            {"id": "alert_002", "experiment_id": "exp_002", "type": "crítica", "description": "Descripción de la alerta 2", "date": datetime.now()}
        ]

        experiments = [
            {"id": "exp_001", "user_id": "user_001", "name": "Experimento 1", "date": datetime.now(), "steps": ["step_001"], "alerts": ["alert_001"], "materials": ["material_001"]},
            {"id": "exp_002", "user_id": "user_002", "name": "Experimento 2", "date": datetime.now(), "steps": ["step_002"], "alerts": ["alert_002"], "materials": ["material_002"]}
        ]

        logs = [
            {"id": "log_001", "experiment_id": "exp_001", "user_id": "user_001", "date_start": datetime.now(), "date_final": None, "steps_completed": ["step_001"], "materials_used": ["material_001"]},
            {"id": "log_002", "experiment_id": "exp_002", "user_id": "user_002", "date_start": datetime.now(), "date_final": None, "steps_completed": ["step_002"], "materials_used": ["material_002"]}
        ]

        materials = [
            {"id": "material_001", "name": "Material 1", "description": "Descripción del material 1"},
            {"id": "material_002", "name": "Material 2", "description": "Descripción del material 2"}
        ]

        organizations = [
            {"id": "org_001", "name": "Organización 1", "users": ["user_001"], "address": "Dirección 1", "contact": "Contacto 1", "creationDate": datetime.now(), "updateDate": datetime.now()},
            {"id": "org_002", "name": "Organización 2", "users": ["user_002"], "address": "Dirección 2", "contact": "Contacto 2", "creationDate": datetime.now(), "updateDate": datetime.now()}
        ]

        steps = [
            {"id": "step_001", "experiment_id": "exp_001", "title": "Paso 1", "description": "Descripción del paso 1"},
            {"id": "step_002", "experiment_id": "exp_002", "title": "Paso 2", "description": "Descripción del paso 2"}
        ]

        users = [
            {"id": "user_001", "name": "Usuario 1", "organization": "org_001", "email": "usuario1@example.com", "creationDate": datetime.now(), "updateDate": datetime.now()},
            {"id": "user_002", "name": "Usuario 2", "organization": "org_002", "email": "usuario2@example.com", "creationDate": datetime.now(), "updateDate": datetime.now()}
        ]

        # Insert data into collections
        for alert in alerts:
            Alert(**alert).save()

        for experiment in experiments:
            Experiment(**experiment).save()

        for log in logs:
            Log(**log).save()

        for material in materials:
            Material(**material).save()

        for organization in organizations:
            Organization(**organization).save()

        for step in steps:
            Step(**step).save()

        for user in users:
            User(**user).save()

        return jsonify({"message": "Data inserted successfully"}), 201
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        return jsonify({"error": str(e)}), 500

# Dynamic GET endpoint
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

    logging.debug(f"Requested collection: {collection_name}")

    collection = collections.get(collection_name)
    if not collection:
        return jsonify({"error": "Collection not found"}), 404
    try:
        documents = collection.objects()
        return jsonify([doc.to_json() for doc in documents])
    except Exception as e:
        return jsonify({"error": "Error retrieving documents"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)