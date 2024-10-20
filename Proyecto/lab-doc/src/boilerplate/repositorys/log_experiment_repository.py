from pymongo import MongoClient
from models import log
from models import experiment

class log_experiment_repository:
    def __init__(self, db_client):
        self.db = db_client['lab_database']  # Acceso a la base de datos
        self.log = log
        self.experiment = experiment

    def create_log(self, log_data):
        """
        Crea una nueva entrada de log en la base de datos.
        """
        return self.log_collection.insert_one(log_data)

    def create_experiment(self, experiment_data):
        """
        Crea un nuevo experimento en la base de datos.
        """
        return self.experiment_collection.insert_one(experiment_data)

    def add_experiment_to_log(self, log_id, experiment_id):
        """
        Añade un experimento a un log específico.
        """
        return self.log_collection.update_one(
            {'_id': log_id},
            {'$push': {'experiments': experiment_id}}
        )

    def get_log_from_user(self, user_id):
        """
        Obtiene todos los logs relacionados con un usuario.
        """
        return self.log_collection.find({'user_id': user_id})

    def get_log_from_organization(self, organization_id):
        """
        Obtiene todos los logs relacionados con una organización.
        """
        return self.log_collection.find({'organization_id': organization_id})

    def get_materials_from_experiment(self, experiment_id):
        """
        Obtiene los materiales usados en un experimento.
        """
        experiment = self.experiment_collection.find_one({'_id': experiment_id})
        if experiment:
            return experiment.get('materials', [])
        return []

    def get_experiment_from_log(self, log_id, experiment_id):
        """
        Obtiene un experimento específico dentro de un log.
        """
        log = self.log_collection.find_one({'_id': log_id, 'experiments': experiment_id})
        return log

    def update_log(self, log_id, log_data):
        """
        Actualiza los datos de un log específico.
        """
        return self.log_collection.update_one(
            {'_id': log_id},
            {'$set': log_data}
        )

    def update_experiment_in_log(self, log_id, experiment_id, experiment_data):
        """
        Actualiza un experimento específico dentro de un log.
        """
        return self.log_collection.update_one(
            {'_id': log_id, 'experiments': experiment_id},
            {'$set': {'experiments.$': experiment_data}}
        )

    def delete_log(self, log_id):
        """
        Elimina un log específico de la base de datos.
        """
        return self.log_collection.delete_one({'_id': log_id})

    def delete_experiment_in_log(self, log_id, experiment_id):
        """
        Descripción: Elimina un experimento dentro de un log específico.
        """
        return self.log_collection.update_one(
            {'_id': log_id},
            {'$pull': {'experiments': experiment_id}}
        )

