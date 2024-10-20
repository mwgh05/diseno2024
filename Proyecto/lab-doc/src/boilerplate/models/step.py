class Step:
    def __init__(self, id, experiment_id, title, description):
        self.id = id
        self.experiment_id = experiment_id
        self.title = title
        self.description = description

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
            json_data['id'],
            json_data['experiment_id'],
            json_data['title'],
            json_data['description']
        )

    def get_description(self):
        return self.description

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description

    def set_title(self, title):
        self.title = title

