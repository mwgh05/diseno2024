from repositorys import material_repository

class MaterialController:
    def __init__(self, material_repository):
        self.material_repository = material_repository

    def create_material(self, material_dto):
        # Lógica para crear un nuevo material
        return self.material_repository.create_material(material_dto)

    def get_material(self, material_id):
        # Lógica para obtener un material por su ID
        return self.material_repository.get_material(material_id)

    def update_material(self, material_id, material_dto):
        # Lógica para actualizar un material
        return self.material_repository.update_material(material_id, material_dto)

    def delete_material(self, material_id):
        # Lógica para eliminar un material
        return self.material_repository.delete_material(material_id)

