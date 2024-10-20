from controllers import experiment_controller
from Data Transfer import experiment_dto

class ExperimentHandler:
    def __init__(self):
        self.experiment_controller = ExperimentController()
        pass

    def create_experiment(self, request):
        """
        Crea un nuevo experimento con los datos proporcionados en la solicitud.
        Esta ruta permite a los usuarios registrar un nuevo experimento en el sistema.
        """
        pass

    def get_experiment(self, experiment_id):
        """
        Obtiene los detalles de un experimento específico usando el ID del experimento.
        Esta ruta recupera toda la información relevante para un experimento en particular.
        """
        pass

    def get_alert(self, experiment_id):
        """
        Recupera las alertas generadas por la IA o por otros procesos del experimento.
        Esta ruta permite a los usuarios ver las advertencias o problemas detectados durante el experimento.
        """
        pass

    def get_IA_questions(self, log_id):
        """
        Obtiene las preguntas generadas por la IA durante el experimento, 
        las cuales necesitan ser resueltas por el usuario. Las preguntas son registradas en el log del experimento.
        """
        pass

    def get_resolve_questions(self, log_id, response):
        """
        Permite al usuario responder las preguntas generadas por la IA, 
        ayudando al sistema a resolver cualquier incertidumbre o duda sobre el proceso experimental.
        """
        pass

    def pause_experiment(self, experiment_id):
        """
        Pausa un experimento en curso. Esta ruta es útil cuando es necesario 
        detener temporalmente el experimento para verificar condiciones o resolver problemas.
        """
        pass

    def update_experiment(self, experiment_id, request):
        """
        Actualiza los datos de un experimento existente. Esta ruta permite modificar 
        cualquier información relevante del experimento después de su creación.
        """
        pass

    def delete_experiment(self, experiment_id):
        """
        Elimina un experimento del sistema usando el ID del experimento.
        Esta ruta permite borrar un experimento y su información asociada.
        """
        pass

