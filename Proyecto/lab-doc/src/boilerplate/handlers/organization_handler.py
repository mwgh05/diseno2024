from controllers import organization_controller
from Data Transfer import organization_dto

class OrganizationHandler:
    def __init__(self, organization_controller):
        self.organization_controller = organization_controller

    def create_organization(self, request):
        """
        Crea una nueva organización con los datos proporcionados en la solicitud.
        Esta ruta permite registrar una organización en el sistema.
        """
        pass

    def create_user_from_organization(self, organization_id, request):
        """
        Crea un nuevo usuario dentro de una organización específica.
        Esta ruta permite agregar un usuario a una organización ya registrada.
        """
        pass

    def get_organization(self, organization_id):
        """
        Obtiene los detalles de una organización específica usando el ID de la organización.
        Esta ruta permite consultar la información de una organización en particular.
        """
        pass

    def get_user_from_organization(self, organization_id, user_id):
        """
        Obtiene la información de un usuario específico dentro de una organización.
        Esta ruta permite consultar los detalles de un usuario asociado a una organización.
        """
        pass

    def update_organization(self, organization_id, request):
        """
        Actualiza los datos de una organización existente.
        Esta ruta permite modificar la información registrada de una organización.
        """
        pass

    def update_user_form_organization(self, organization_id, user_id, request):
        """
        Actualiza los detalles de un usuario específico dentro de una organización.
        Esta ruta permite modificar la información de un usuario registrado en una organización.
        """
        pass

    def delete_organization(self, organization_id):
        """
        Elimina una organización del sistema usando el ID de la organización.
        Esta ruta permite borrar una organización y toda su información asociada.
        """
        pass

    def delete_user_form_organization(self, organization_id, user_id):
        """
        Elimina un usuario de una organización utilizando el ID de la organización y del usuario.
        Esta ruta permite remover un usuario específico de una organización.
        """
        pass

