class Ai_connector:
    def __init__(self, mediapipe_client):
        self.mediapipe_client = mediapipe_client  # MediaPipe Client

    def send_video_stream(self, video_stream):
        """
        Descripción: Envía el stream de video al servicio de MediaPipe para análisis.
        """
        # Lógica para enviar el video a MediaPipe
        response = self.mediapipe_client.process_video(video_stream)
        return response

    def receive_ai_results(self):
        """
        Descripción: Recibe los resultados procesados por MediaPipe.
        """
        # Obtener los resultados del análisis
        ai_results = self.mediapipe_client.get_results()
        return ai_results

    def train_ai_model(self, training_data):
        """
        Descripción: Entrena el modelo de IA en MediaPipe con los datos de entrenamiento proporcionados.
        """
        # Lógica para entrenar el modelo en MediaPipe
        self.mediapipe_client.train_model(training_data)
