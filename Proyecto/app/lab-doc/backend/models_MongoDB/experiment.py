from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()

class Experiment(db.Document):
    id = db.StringField(required=True, unique=True)
    user_id = db.StringField(required=True)
    name = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.now)
    steps = db.ListField(db.StringField(), default=list)
    alerts = db.ListField(db.StringField(), default=list)
    materials = db.ListField(db.StringField(), default=list)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "steps": self.steps,
            "alerts": self.alerts,
            "materials": self.materials,
            "date": self.date
        }

    @staticmethod
    def from_json(json_data):
        return Experiment(
            id=json_data['id'],
            user_id=json_data['user_id'],
            name=json_data['name'],
            steps=json_data.get('steps', []),
            alerts=json_data.get('alerts', []),
            materials=json_data.get('materials', []),
            date=json_data.get('date', datetime.utcnow())
        )

    def add_step(self, step_id):
        self.steps.append(step_id)
        self.save()

    def add_material(self, material_id):
        self.materials.append(material_id)
        self.save()

    def add_alert(self, alert_id):
        self.alerts.append(alert_id)
        self.save()

    def set_date(self, date_final):
        self.date = date_final
        self.save()

    def get_steps(self):
        return self.steps

    def get_materials(self):
        return self.materials

    def get_alerts(self):
        return self.alerts