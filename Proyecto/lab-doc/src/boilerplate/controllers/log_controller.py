from repositorys import log_repository

class LogController:
    def __init__(self, log_experiment_repository):
        self.log_experiment_repository = log_experiment_repository

    def create_log(self, log_dto):
        # Lógica para crear una nueva bitácora
        return self.log_experiment_repository.create_log(log_dto)

    def get_log(self, log_id):
        # Lógica para obtener una bitácora
        return self.log_experiment_repository.get_log(log_id)

    def generate_log(self, log_id, log_dto):
        # Lógica para generar una nueva bitácora
        return self.log_experiment_repository.generate_log(log_id, log_dto)

    def update_log(self, log_id, log_dto):
        # Lógica para actualizar una bitácora
        return self.log_experiment_repository.update_log(log_id, log_dto)

    def delete_log(self, log_id):
        # Lógica para eliminar una bitácora
        return self.log_experiment_repository.delete_log(log_id)
