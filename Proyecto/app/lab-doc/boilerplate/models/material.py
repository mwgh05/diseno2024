class Material:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    @staticmethod
    def from_json(json_data):
        return Material(
            json_data['id'],
            json_data['name'],
            json_data['description']
        )

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

