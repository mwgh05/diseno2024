from pymongo import MongoClient

class OrganizationRepository:
    def __init__(self, db_client):
        self.db = db_client['lab_database']  # Conexión a la base de datos
        self.organizations = organizations

    def create_organization(self, organization_data):
        """
        Crea una nueva organización en la base de datos.
        """
        return self.organizations_collection.insert_one(organization_data)

    def create_user_from_organization(self, organization_id, user_data):
        """
        Añade un usuario a una organización existente.
        """
        return self.organizations_collection.update_one(
            {'_id': organization_id},
            {'$push': {'users': user_data}}
        )

    def get_organization(self, organization_id):
        """
        Obtiene una organización específica basada en su ID.
        """
        return self.organizations_collection.find_one({'_id': organization_id})

    def get_user_from_organization(self, organization_id, user_id):
        """
        Obtiene un usuario de una organización específica.
        """
        return self.organizations_collection.find_one(
            {'_id': organization_id, 'users._id': user_id},
            {'users.$': 1}
        )

    def update_organization(self, organization_id, organization_data):
        """
        Actualiza la información de una organización específica.
        """
        return self.organizations_collection.update_one(
            {'_id': organization_id},
            {'$set': organization_data}
        )

    def update_user_from_organization(self, organization_id, user_id, user_data):
        """
        Actualiza un usuario específico de una organización.
        """
        return self.organizations_collection.update_one(
            {'_id': organization_id, 'users._id': user_id},
            {'$set': {'users.$': user_data}}
        )

    def delete_organization(self, organization_id):
        """
        Elimina una organización específica de la base de datos.
        """
        return self.organizations_collection.delete_one({'_id': organization_id})

    def delete_user_from_organization(self, organization_id, user_id):
        """
        Elimina un usuario específico de una organización.
        """
        return self.organizations_collection.update_one(
            {'_id': organization_id},
            {'$pull': {'users': {'_id': user_id}}}
        )

