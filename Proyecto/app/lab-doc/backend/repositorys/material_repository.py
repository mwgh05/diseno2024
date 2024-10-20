from pymongo import MongoClient
from models import material

class material_repository:
    def __init__(self, db_client):
        self.db = db_client['lab_database']  # Acceso a la base de datos
        self.materials = materials

    def create_material(self, material_data):
        """
        Crea un nuevo material en la base de datos.
        """
        return self.materials_collection.insert_one(material_data)

    def get_material_by_id(self, material_id):
        """
        Obtiene un material específico basado en su ID.
        """
        return self.materials_collection.find_one({'_id': material_id})

    def update_material(self, material_id, material_data):
        """
        Actualiza la información de un material específico.
        """
        return self.materials_collection.update_one(
            {'_id': material_id},
            {'$set': material_data}
        )

    def delete_material(self, material_id):
        """
        Elimina un material específico de la base de datos.
        """
        return self.materials_collection.delete_one({'_id': material_id})

