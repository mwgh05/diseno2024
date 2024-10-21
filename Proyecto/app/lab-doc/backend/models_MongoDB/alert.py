from flask_mongoengine import MongoEngine

db = MongoEngine()

class Alert(db.Document):
    id = db.StringField(required=True)  # ID único de la alerta
    experiment_id = db.StringField(required=True)  # ID del experimento relacionado
    type = db.StringField(required=True)  # Tipo de alerta (informativa, crítica, etc.)
    description = db.StringField(required=True)  # Descripción de la alerta
    date = db.DateTimeField(required=True)  # Fecha de la alerta

    def to_json(self):
        return {
            "id": self.id,
            "experiment_id": self.experiment_id,
            "type": self.type,
            "description": self.description,
            "date": self.date
        }

    @staticmethod
    def from_json(json_data):
        return Alert(
            id=json_data['id'],
            experiment_id=json_data['experiment_id'],
            type=json_data['type'],
            description=json_data['description'],
            date=json_data['date']
        )
