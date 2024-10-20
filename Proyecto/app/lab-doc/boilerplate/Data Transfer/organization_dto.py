class organization_dto:
    def __init__(self, organization_id, user_id, email):
        self.organization_id = organization_id
        self.user_id = user_id
        self.email = email

    @staticmethod
    def from_json(json_data):
        """
        Convierte los datos JSON en una instancia de OrganizationDTO.
        """
        return OrganizationDTO(
            organization_id=json_data.get('organization_id'),
            user_id=json_data.get('user_id'),
            email=json_data.get('email')
        )

    def to_json(self):
        """
        Convierte la instancia de OrganizationDTO en formato JSON.
        """
        return {
            'organization_id': self.organization_id,
            'user_id': self.user_id,
            'email': self.email
        }

    def validate(self):
        """
        Valida los datos del DTO para asegurar que son correctos.
        """
        if not self.organization_id:
            raise ValueError("El ID de la organización es obligatorio.")
        if not self.user_id:
            raise ValueError("El ID del usuario es obligatorio.")
        if not self.email:
            raise ValueError("El correo electrónico es obligatorio.")

