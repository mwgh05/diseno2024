from repositorys import organization_repository

class OrganizationController:
    def __init__(self, organization_repository):
        self.organization_repository = organization_repository

    def create_organization(self, organization_dto):
        # Lógica para crear una nueva organización
        return self.organization_repository.create_organization(organization_dto)

    def create_user_from_organization(self, organization_id, user_dto):
        # Lógica para crear un usuario dentro de una organización
        return self.organization_repository.create_user_from_organization(organization_id, user_dto)

    def get_organization(self, organization_id):
        # Lógica para obtener una organización por su ID
        return self.organization_repository.get_organization(organization_id)

    def get_user_from_organization(self, organization_id, user_id):
        # Lógica para obtener un usuario asociado a una organización
        return self.organization_repository.get_user_from_organization(organization_id, user_id)

    def update_organization(self, organization_id, organization_dto):
        # Lógica para actualizar los detalles de una organización
        return self.organization_repository.update_organization(organization_id, organization_dto)

    def update_user_form_organization(self, organization_id, user_id, user_dto):
        # Lógica para actualizar los detalles de un usuario asociado a una organización
        return self.organization_repository.update_user_form_organization(organization_id, user_id, user_dto)

    def delete_organization(self, organization_id):
        # Lógica para eliminar una organización
        return self.organization_repository.delete_organization(organization_id)

    def delete_user_form_organization(self, organization_id, user_id):
        # Lógica para eliminar un usuario asociado a una organización
        return self.organization_repository.delete_user_form_organization(organization_id, user_id)

