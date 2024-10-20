import alert
import material
import step

class Experiment:
    def __init__(self, id, user_id, name, date, steps=None, alerts=None, materials=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.steps = steps if steps else []
        self.alerts = alerts if alerts else []
        self.materials = materials if materials else []
        self.date = date

    def to_json(self):
        """
        Convierte la instancia de la clase Experiment a formato JSON.
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "steps": self.steps,
            "alerts": self.alerts,
            "materials": self.materials,
            "date": self.date
        }

    @classmethod
    def from_json(cls, json_data):
        """
        Crea una instancia de Experiment a partir de un objeto JSON.
        """
        return cls(
            id=json_data.get("id"),
            user_id=json_data.get("user_id"),
            name=json_data.get("name"),
            steps=json_data.get("steps", []),
            alerts=json_data.get("alerts", []),
            materials=json_data.get("materials", []),
            date=json_data.get("date")
        )

    def add_step(self, step_id):
        """
        Añade un nuevo paso al experimento.
        """
        self.steps.append(step_id)

    def add_material(self, material_id):
        """
        Añade un nuevo material al experimento.
        """
        self.materials.append(material_id)

    def add_alert(self, alert_id):
        """
        Añade una nueva alerta al experimento.
        """
        self.alerts.append(alert_id)

    def set_date(self, date_final):
        """
        Establece la fecha final del experimento.
        """
        self.date = date_final

    def get_steps(self):
        """
        Devuelve la lista de pasos del experimento.
        """
        return self.steps

    def get_materials(self):
        """
        Devuelve la lista de materiales del experimento.
        """
        return self.materials

    def get_alerts(self):
        """
        Devuelve la lista de alertas del experimento.
        """
        return self.alerts

