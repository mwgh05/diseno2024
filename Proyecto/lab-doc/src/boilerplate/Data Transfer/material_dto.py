class material_dto:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def from_json(json_data):
        """
        Convierte los datos JSON en una instancia de MaterialDTO.
        """
        return MaterialDTO(
            id=json_data.get('id'),
            name=json_data.get('name'),
            description=json_data.get('description')
        )

    def to_json(self):
        """
        Convierte la instancia de MaterialDTO en formato JSON.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def validate(self):
        """
        Valida los datos del DTO para asegurar que son correctos.
        """
        if not self.name:
            raise ValueError("El nombre del material es obligatorio.")
        if not self.description:
            raise ValueError("La descripción del material es obligatoria.")

