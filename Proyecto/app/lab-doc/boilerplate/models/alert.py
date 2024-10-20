class Alert:
    def __init__(self, id, experiment_id, type, description, date):
        self.id = id
        self.experiment_id = experiment_id
        self.type = type
        self.description = description
        self.date = date

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
            json_data['id'],
            json_data['experiment_id'],
            json_data['type'],
            json_data['description'],
            json_data['date']
        )

    def set_date(self, date):
        self.date = date

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

    def set_type(self, type):
        self.type = type

    def set_desc

