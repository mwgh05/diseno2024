class log_dto:
    def __init__(self, id, experiment_id, user_id):
        self.id = id
        self.experiment_id = experiment_id
        self.user_id = user_id

    @staticmethod
    def from_json(json_data):
        """
        Convierte los datos JSON proporcionados en una instancia de LogDTO.
        Este método toma los datos de un request JSON y los convierte en un objeto LogDTO.
        """
        return LogDTO(
            id=json_data.get('id'),
            experiment_id=json_data.get('experiment_id'),
            user_id=json_data.get('user_id')
        )

    def to_json(self):
        """
        Convierte la instancia de LogDTO en formato JSON para enviarlo como respuesta.
        Este método es útil para devolver los datos del log al cliente en formato JSON.
        """
        return {
            'id': self.id,
            'experiment_id': self.experiment_id,
            'user_id': self.user_id
        }

    def validate(self):
        """
        Valida los datos del DTO para asegurar que todos los campos requeridos 
        están presentes y son correctos antes de procesar la información.
        Lanza excepciones si los datos son inválidos.
        """
        if not self.experiment_id:
            raise ValueError("El ID del experimento es obligatorio.")
        if not self.user_id:
            raise ValueError("El ID del usuario es obligatorio.")
        # Puedes agregar más validaciones según sea necesario

