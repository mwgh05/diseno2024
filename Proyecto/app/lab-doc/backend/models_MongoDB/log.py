from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()

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

    @staticmethod
    def from_json(json_data):
        return Log(
            id=json_data['id'],
            experiment_id=json_data['experiment_id'],
            user_id=json_data['user_id'],
            date_start=json_data['date_start'],
            date_final=json_data.get('date_final'),
            detail=json_data.get('detail'),
            steps_completed=json_data.get('steps_completed', []),
            materials_used=json_data.get('materials_used', [])
        )

    def set_date_final(self, date_final):
        self.date_final = date_final
        self.save()