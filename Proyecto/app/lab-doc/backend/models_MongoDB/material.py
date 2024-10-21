from flask_mongoengine import MongoEngine

db = MongoEngine()

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

    @staticmethod
    def from_json(json_data):
        return Material(
            id=json_data['id'],
            name=json_data['name'],
            description=json_data['description']
        )

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name
        self.save()

    def set_description(self, description):
        self.description = description
        self.save()