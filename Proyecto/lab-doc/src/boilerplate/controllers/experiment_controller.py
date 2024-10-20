from repositorys import experiment_repository

class ExperimentController:
    def __init__(self, log_experiment_repository):
        self.log_experiment_repository = log_experiment_repository

    def create_experiment(self, experiment_dto):
        # Lógica para crear un experimento
        return self.log_experiment_repository.create_experiment(experiment_dto)

    def get_experiment(self, experiment_id):
        # Lógica para obtener un experimento por su ID
        return self.log_experiment_repository.get_experiment(experiment_id)

    def get_alert(self, experiment_id):
        # Lógica para obtener alertas de un experimento
        return self.log_experiment_repository.get_alert(experiment_id)

    def get_IA_questions(self, experiment_id):
        # Lógica para obtener preguntas de la IA sobre el experimento
        return self.log_experiment_repository.get_IA_questions(experiment_id)

    def add_step(self, experiment_id, step_data):
        # Lógica para agregar un paso al experimento
        return self.log_experiment_repository.add_step(experiment_id, step_data)

    def add_material(self, experiment_id, material_id):
        # Lógica para agregar un material al experimento
        return self.log_experiment_repository.add_material(experiment_id, material_id)

    def get_resolve_questions(self, experiment_id, response_dto):
        # Lógica para resolver preguntas de la IA
        return self.log_experiment_repository.get_resolve_questions(experiment_id, response_dto)

    def pause_experiment(self, experiment_id):
        # Lógica para pausar el experimento
        return self.log_experiment_repository.pause_experiment(experiment_id)

    def update_experiment(self, experiment_id, experiment_dto):
        # Lógica para actualizar el experimento
        return self.log_experiment_repository.update_experiment(experiment_id, experiment_dto)

    def delete_experiment(self, experiment_id):
        # Lógica para eliminar un experimento
        return self.log_experiment_repository.delete_experiment(experiment_id)

