from pymongo import MongoClient
from datetime import datetime

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['Prueba']

# Datos de ejemplo para cada colección
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

# Insertar datos en las colecciones
db.alerts.insert_many(alerts)
db.experiments.insert_many(experiments)
db.logs.insert_many(logs)
db.materials.insert_many(materials)
db.organizations.insert_many(organizations)
db.steps.insert_many(steps)
db.users.insert_many(users)

print("Datos insertados correctamente")