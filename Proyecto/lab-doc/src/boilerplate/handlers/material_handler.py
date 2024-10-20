from controllers import material_controller
from Data Transfer import material_dto

class MaterialHandler:
    def __init__(self, material_controller):
        self.material_controller = material_controller

    def create_material(self, request):
        """
        Crea un nuevo material con los datos proporcionados en la solicitud.
        Esta ruta permite registrar un nuevo material en el sistema, como parte de los recursos necesarios para los experimentos.
        """
        pass

    def get_material(self, material_id):
        """
        Obtiene los detalles de un material específico utilizando el ID del material.
        Esta ruta permite consultar la información de un material almacenado en el sistema.
        """
        pass

    def update_material(self, material_id, request):
        """
        Actualiza los datos de un material existente. 
        Esta ruta permite modificar la información del material, como su nombre o descripción.
        """
        pass

    def delete_material(self, material_id):
        """
        Elimina un material del sistema utilizando el ID del material.
        Esta ruta permite borrar un material que ya no es necesario.
        """
        pass

