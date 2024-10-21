from flask_mongoengine import MongoEngine

db = MongoEngine()

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

    @staticmethod
    def from_json(json_data):
        return Step(
            id=json_data['id'],
            experiment_id=json_data['experiment_id'],
            title=json_data['title'],
            description=json_data['description']
        )

    def get_description(self):
        return self.description

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description
        self.save()

    def set_title(self, title):
        self.title = title
        self.save()