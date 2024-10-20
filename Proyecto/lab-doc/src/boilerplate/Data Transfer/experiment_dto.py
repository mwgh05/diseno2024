class experiment_dto:
    def __init__(self, id, user_id, name):
        self.id = id
        self.user_id = user_id
        self.name = name

    @staticmethod
    def from_json(json_data):
        """
        Convierte los datos JSON en una instancia de ExperimentDTO.
        """
        return ExperimentDTO(
            id=json_data.get('id'),
            user_id=json_data.get('user_id'),
            name=json_data.get('name')
        )

    def to_json(self):
        """
        Convierte la instancia de ExperimentDTO en formato JSON.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name
        }

    def validate(self):
        """
        Valida los datos del DTO para asegurar que son correctos.
        """
        if not self.name:
            raise ValueError("El nombre del experimento es obligatorio.")
        if not self.user_id:
            raise ValueError("El ID del usuario es obligatorio.")

