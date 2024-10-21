import experiment

class Log:
    def __init__(self, id, experiment_id, user_id, date_start, date_final=None, detail=None, steps_completed=None, materials_used=None):
        self.id = id
        self.experiment_id = experiment_id
        self.user_id = user_id
        self.date_start = date_start
        self.date_final = date_final
        self.detail = detail
        self.steps_completed = steps_completed if steps_completed is not None else []
        self.materials_used = materials_used if materials_used is not None else []

    def to_json(self):
        """
        Convierte la instancia de la clase Log a formato JSON.
        """
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

    @classmethod
    def from_json(cls, json_data):
        """
        Crea una instancia de Log a partir de un objeto JSON.
        """
        return cls(
            id=json_data.get("id"),
            experiment_id=json_data.get("experiment_id"),
            user_id=json_data.get("user_id"),
            date_start=json_data.get("date_start"),
            date_final=json_data.get("date_final"),
            detail=json_data.get("detail"),
            steps_completed=json_data.get("steps_completed", []),
            materials_used=json_data.get("materials_used", [])
        )

    def set_date_final(self, date_final):
        """
        Establece la fecha final de la bitácora.
        """
        self.date_final = date_final